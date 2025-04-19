# 📁 reminder.json (file lưu nhắc việc nâng cao)
# Mẫu dữ liệu:
[
  {
    "id": 1,
    "text": "Uống nghệ mật ong",
    "time": "06:30",
    "repeat": "daily",
    "repeat_count": none,
    "expires": none,
    "days_of_week": none,
    "status": "active"
  },
  {
    "id": 2,
    "text": "Review tuần",
    "time": "20:00",
    "repeat": "weekly",
    "repeat_count": none,
    "expires": none,
    "days_of_week": ["sunday"],
    "status": "active"
  }
]

# 📁 scheduler.py
import json
import time
import requests
from datetime import datetime

BOT_TOKEN = 'AAH5HNjaLENJpQyoCgDyvqq1MwWJ2RMLNeM'
CHAT_ID = 5582140961  # ví dụ: 123456789
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


# 📁 reminder_parser.py
# Tạo nhắc việc bằng ngôn ngữ tự nhiên → xuất thành reminder cấu trúc
import re
from datetime import datetime, timedelta
import uuid

VIETDAY = {
    "thứ hai": "monday",
    "thứ ba": "tuesday",
    "thứ tư": "wednesday",
    "thứ năm": "thursday",
    "thứ sáu": "friday",
    "thứ bảy": "saturday",
    "chủ nhật": "sunday"
}

def parse_natural_reminder(text):
    result = {
        "id": int(str(uuid.uuid4().int)[:6]),
        "text": "",
        "time": "",
        "repeat": None,
        "repeat_count": None,
        "expires": None,
        "days_of_week": None,
        "status": "active"
    }

    # Tách phần nội dung cần nhắc
    match_text = re.search(r"nhắc.*?là\s(.+)", text)
    if match_text:
        result["text"] = match_text.group(1).strip()
    else:
        result["text"] = text.strip()

    # Tìm giờ dạng HH:MM
    match_time = re.search(r"(\d{1,2})[h:](\d{2})", text)
    if match_time:
        hour = match_time.group(1).zfill(2)
        minute = match_time.group(2).zfill(2)
        result["time"] = f"{hour}:{minute}"

    # Lặp mỗi ngày / tuần
    if "mỗi ngày" in text or "hằng ngày" in text:
        result["repeat"] = "daily"
    if "hàng tuần" in text or "mỗi tuần" in text:
        result["repeat"] = "weekly"

    # Ngày cụ thể trong tuần
    days = [v for k, v in VIETDAY.items() if k in text]
    if days:
        result["repeat"] = "weekly"
        result["days_of_week"] = days

    # Số lần nhắc
    match_count = re.search(r"(\d+) lần", text)
    if match_count:
        result["repeat_count"] = int(match_count.group(1))

    # Hết hạn vào ngày nào
    match_expire = re.search(r"đến ngày (\d{1,2})[/-](\d{1,2})[/-](\d{4})", text)
    if match_expire:
        d, m, y = match_expire.groups()
        result["expires"] = f"{y}-{m.zfill(2)}-{d.zfill(2)}"

    return result

if __name__ == '__main__':
    test = "Nhắc mỗi thứ bảy lúc 19h gọi điện cho mẹ, lặp hàng tuần vĩnh viễn"
    print(parse_natural_reminder(test))
