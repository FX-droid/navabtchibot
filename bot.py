TOKEN = "8224987770:AAENbToS_BXrz4ybJ7cdSIKEtq9HPv15Y5Y"
CHAT_ID = "-4994363474"

import datetime
import time
import requests
import os


print("Bot ishga tushdi...")

# 🧪 TEST UCHUN: bugun darhol yuborish
def send_now(test=False):
    today = datetime.date.today()

    with open("index.txt") as f:
        index = int(f.read().strip())

    with open("navbatchilar.txt", encoding="utf-8") as f:
        names = f.read().splitlines()

    if not names:
        return

    name = names[index % len(names)]

    with open("index.txt", "w") as f:
        f.write(str(index + 1))

    text = f"""🧪 TEST XABAR
🌞 Xayrli tong!
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

    with open("last_sent.txt", "w") as f:
        f.write(today.isoformat())

    print("TEST yuborildi:", name)


# 🧪 Agar last_sent.txt bo‘sh bo‘lsa — test yuboradi
if not os.path.exists("last_sent.txt") or os.stat("last_sent.txt").st_size == 0:
    send_now(test=True)


# 🔁 ASOSIY LOOP (09:05)
while True:
    now = datetime.datetime.now()
    today = now.date()

    # ❌ Shanba
    if today.weekday() == 5:
        time.sleep(60)
        continue

    # ⏰ 09:05
    if now.hour == 9 and now.minute == 13:

        if os.path.exists("last_sent.txt"):
            with open("last_sent.txt") as f:
                if f.read().strip() == today.isoformat():
                    time.sleep(60)
                    continue

        send_now()
        time.sleep(60)

    time.sleep(10)
