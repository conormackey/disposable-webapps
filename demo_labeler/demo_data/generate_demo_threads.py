#!/usr/bin/env python3
"""
Generate synthetic threads for the demo labeler.
Output: demo_threads.json (same schema as the original validation sample).
"""
import json, random, itertools, datetime
from pathlib import Path

random.seed(123)

out_dir = Path(__file__).parent
out_dir.mkdir(parents=True, exist_ok=True)

REGIONS = ['North America', 'Europe', 'APAC']
TOPICS = ['innovation', 'packaging', 'marketing', 'pricing', 'usability', 'sustainability']
GROUPS = ['T2','T3']
start_date = datetime.date(2025, 5, 10)

threads = []
for g in GROUPS:
    for u_idx in range(1,6):
        user = f"demo_{g.lower()}_{u_idx:02d}@example.com"
        for t_idx in range(1,3):
            thread_id = f"thread_{t_idx}"
            region = random.choice(REGIONS)
            date = start_date + datetime.timedelta(days=random.randint(0,6))
            msgs = []
            n_msgs = random.randint(4,8)
            hour = random.randint(7,20)
            for m in range(n_msgs):
                prompt_topic = random.choice(TOPICS)
                resp_topic = random.choice(TOPICS)
                msgs.append({
                    'id': f"msg_{len(msgs)+1}",
                    'prompt': f"[{user}] Ask about {prompt_topic} scenario {m+1}",
                    'response': f"AI reply with {resp_topic} idea {m+1}",
                    'date': date.isoformat(),
                    'time': f"{(hour + m//2)%24:02d}:{(m*7)%60:02d}"
                })
            threads.append({
                'key': f"{g}|{user}|{thread_id}",
                'user': user,
                'thread_id': thread_id,
                'group': g,
                'region': region,
                'dateYMD': date.isoformat(),
                'msgs': msgs
            })

(out_dir / 'demo_threads.json').write_text(json.dumps({'sample': threads}, indent=2))
print(f"Wrote {out_dir/'demo_threads.json'} (threads={len(threads)})")
