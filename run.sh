#!/usr/bin/env bash

echo "تثبيت المتطلبات إذا وجدت..."
if [[ -f requirements.txt ]]; then
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi

echo "تشغيل main.py..."
python3 main.py
