# Demo slides and prompt templates

Contents
- `make_slides.py` — builds `llm_disposable_webapps_demo.pptx` (requires `python-pptx`).
- `prompts/` — copy/paste prompt templates for web-app generation.

Usage
```bash
# from repo root, with python3 available
pip install python-pptx   # if not already installed
python demo_slides/make_slides.py
```
The PPTX will be written to `demo_slides/llm_disposable_webapps_demo.pptx`.

Templates
- `prompts/template_web_app.txt` — full disposable web app brief.
- `prompts/template_data_briefing.txt` — data-schema briefing block.
- `prompts/template_surprise_me.txt` — optional “surprise me” add-on.

Feel free to add more templates or slides and re-run the script. The theme/layout is intentionally plain so you can restyle in PowerPoint/Keynote afterward.
