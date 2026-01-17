# TOKEN = "8224987770:AAENbToS_BXrz4ybJ7cdSIKEtq9HPv15Y5Y"
# CHAT_ID = "-4994363474"

import datetime
import requests
import os
import sys

TOKEN = os.environ.get("8224987770:AAENbToS_BXrz4ybJ7cdSIKEtq9HPv15Y5Y")
CHAT_ID = os.environ.get("-4994363474")

now = datetime.datetime.now()
today = now.date()

# ❌ Shanba
if today.weekday() == 5:
    sys.exit()

# ⏰ Faqat 09:05
if not (now.hour == 9 and now.minute == 5):
    sys.exit()

# 🔁 Bugun yuborilganmi?
if os.path.exists("last_sent.txt"):
    with open("last_sent.txt") as f:
        if f.read().strip() == today.isoformat():
            sys.exit()

# Index
with open("index.txt") as f:
    index = int(f.read().strip())

# Ismlar
with open("navbatchilar.txt", encoding="utf-8") as f:
    names = f.read().splitlines()

if not names:
    sys.exit()

name = names[index % len(names)]

# Keyingi kunga o‘tkazish
with open("index.txt", "w") as f:
    f.write(str(index + 1))

text = f"""🌞 Xayrli tong!
Kuningiz xayrli o‘tsin.
🍽 Bugun navbatchilik **{name}** qiladi."""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
)

# Bugun yuborildi deb belgilash
with open("last_sent.txt", "w") as f:
    f.write(today.isoformat())
