# 📁 reminder.json (file lưu nhắc việc nâng cao)
# Mẫu dữ liệu:
[
  {
    "id": 1,
    "text": "Uống nghệ mật ong",
    "time": "06:30",
    "repeat": "daily",
    "repeat_count": null,
    "expires": null,
    "days_of_week": null,
    "status": "active"
  },
  {
    "id": 2,
    "text": "Review tuần",
    "time": "20:00",
    "repeat": "weekly",
    "repeat_count": null,
    "expires": null,
    "days_of_week": ["sunday"],
    "status": "active"
  }
]

# 📁 scheduler.py
import json
import time
import requests
from datetime import datetime

BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
CHAT_ID = YOUR_CHAT_ID_HERE  # ví dụ: 123456789
REMINDER_FILE = 'reminder.json'

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)

def load_reminders():
    with open(REMINDER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(reminders, f, indent=2, ensure_ascii=False)

def should_send(reminder, now):
    if reminder["status"] != "active":
        return False

    now_time = now.strftime("%H:%M")
    now_day = now.strftime("%A").lower()  # ví dụ: 'monday'

    # Kiểm tra thời gian đúng giờ
    if reminder["time"] != now_time:
        return False

    # Kiểm tra ngày trong tuần nếu repeat là weekly
    if reminder["repeat"] == "weekly":
        if reminder.get("days_of_week") and now_day not in reminder["days_of_week"]:
            return False

    # Kiểm tra hạn
    if reminder.get("expires"):
        expire_date = datetime.strptime(reminder["expires"], "%Y-%m-%d")
        if now.date() > expire_date.date():
            return False

    # Kiểm tra số lần nhắc còn lại
    if reminder.get("repeat_count") is not None:
        if reminder["repeat_count"] <= 0:
            return False

    return True

def process_reminders():
    reminders = load_reminders()
    now = datetime.now()

    for reminder in reminders:
        if should_send(reminder, now):
            send_telegram_message(f"🔔 Nhắc việc: {reminder['text']}")

            # Giảm số lần lặp nếu có
            if reminder.get("repeat_count") is not None:
                reminder["repeat_count"] -= 1
                if reminder["repeat_count"] <= 0:
                    reminder["status"] = "done"

    save_reminders(reminders)

if __name__ == '__main__':
    print("🧠 Sambot Scheduler đang chạy...")
    while True:
        process_reminders()
        time.sleep(60)  # kiểm tra mỗi phút
