import datetime
import requests

TOKEN = "8224987770:AAENbToS_BXrz4ybJ7cdSIKEtq9HPv15Y5Y"
CHAT_ID = "-4994363474"

now = datetime.datetime.now()
today = now.date()

# ❌ Shanba (5)
if today.weekday() == 5:
    exit()

# ⏰ Faqat 20:00 da
if not (now.hour == 21 and now.minute == 35):
    exit()

# 🔁 Bugun allaqachon yuborilganmi?
if os.path.exists("last_sent.txt"):
    with open("last_sent.txt") as f:
        if f.read().strip() == today.isoformat():
            exit()

# Index
with open("index.txt") as f:
    index = int(f.read().strip())

with open("navbatchilar.txt", encoding="utf-8") as f:
    names = f.read().splitlines()

if not names:
    exit()

name = names[index % len(names)]

with open("index.txt", "w") as f:
    f.write(str(index + 1))

text = f"""🌙 Xayrli kech!
Ertangi kuningiz xayrli o‘tsin.
🍽 Ertaga navbatchilik **{name}** qiladi."""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
)

# Bugun yuborildi
with open("last_sent.txt", "w") as f:
    f.write(today.isoformat())
