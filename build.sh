#!/bin/bash
# activate the virtual environment
source ./venv/bin/activate
export FlASK_APP=main.py
pip install -r requirements.txt

# migrate and collect static
flask db init
flask db migrate
flask db upgrade
