@echo off
pip install -r requirements.txt
pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
python main.py
