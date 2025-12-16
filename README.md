# LLM Disposable Web App Demos

Everything you need to demo the “single-use web app” workflow with synthetic data only.

## Contents
- `demo_labeler/` — chat-style manual labeler (user right, AI left). Synthetic threads + synthetic T2/T3 Excel exports.
- `demo_time_window_viewer/` — time-window explorer with bars/scatter/region buckets + thread browser. Synthetic data only.
- `demo_slides/` — PowerPoint deck (`llm_disposable_webapps_demo.pptx`), slide generator script, and prompt templates.
- `demo_slides/prompts/` — copy/paste prompt templates with placeholders for your own projects.

## Quick start
1) Run the demos (each folder self-contained):
   ```bash
   cd demo_labeler
   python3 -m http.server 8000
   # open http://localhost:8000 and click “Load Demo”

   cd ../demo_time_window_viewer
   python3 -m http.server 8000
   # open http://localhost:8000 and click “Load demo T2 + T3”
   ```
   All data is synthetic; nothing sensitive is included.

2) Slides:
   - Edit/use `demo_slides/llm_disposable_webapps_demo.pptx`.
   - To regenerate from script (after editing text in `make_slides.py`):
     ```bash
     pip install python-pptx
     python demo_slides/make_slides.py
     ```

3) Prompt templates:
   - `template_web_app.txt` — full disposable web-app brief with placeholders for goal, data, requirements.
   - `template_data_briefing.txt` — concise schema briefing block.
   - `template_surprise_me.txt` — optional “extra view” add-on.

## Synthetic datasets included
- `demo_labeler/demo_data/demo_threads.json` — small chat sample for the labeler demo.
- `demo_labeler/demo_data/synthetic_experiment_T2_with_threads.xlsx`
- `demo_labeler/demo_data/synthetic_experiment_T3_with_threads.xlsx`
  (columns: FakeEmail, thread_id, __msg_id, prompt, response, Date, Time of Day, Region, Function, Member)
- `demo_time_window_viewer/demo_data/` — synthetic T2/T3 JSON label/chat pairs for the explorer.

## Third example
A third example is referenced in the slides as a placeholder; it is not included in this bundle. Add your own project example later if desired.

## License / sensitivity
All data here is synthetic and safe to share. Replace with real data only in private forks; keep PII out of prompts and outputs.
