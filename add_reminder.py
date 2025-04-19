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


# 📁 reminder_parser.py


# 📁 add_reminder.py
# Nhận đầu vào từ GPT (dạng ngôn ngữ tự nhiên), phân tích và lưu vào reminder.json
from reminder_parser import parse_natural_reminder
import json

REMINDER_FILE = 'reminder.json'

def load_reminders():
    with open(REMINDER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(reminders, f, indent=2, ensure_ascii=False)

def add_reminder_from_text(natural_text):
    new_reminder = parse_natural_reminder(natural_text)
    reminders = load_reminders()
    reminders.append(new_reminder)
    save_reminders(reminders)
    return new_reminder

if __name__ == '__main__':
    test_input = "Nhắc mỗi thứ bảy lúc 19h gọi điện cho mẹ, nhắc 3 lần"
    created = add_reminder_from_text(test_input)
    print("Đã tạo nhắc việc:", created)
