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
<... (không đổi - giữ nguyên như trước) ...>

# 📁 reminder_parser.py
<... (không đổi - giữ nguyên như trước) ...>

# 📁 add_reminder.py
<... (không đổi - giữ nguyên như trước) ...>

# 📁 delete_reminder.py
<... (không đổi - giữ nguyên như trước) ...>

# 📁 edit_reminder.py
# Cập nhật nội dung nhắc việc theo ID
import json

REMINDER_FILE = 'reminder.json'

def load_reminders():
    with open(REMINDER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(reminders, f, indent=2, ensure_ascii=False)

def edit_reminder(reminder_id, updates):
    reminders = load_reminders()
    found = False

    for reminder in reminders:
        if reminder['id'] == reminder_id:
            for key, value in updates.items():
                if key in reminder:
                    reminder[key] = value
            found = True
            break

    if found:
        save_reminders(reminders)
        print(f"✅ Đã cập nhật nhắc việc ID: {reminder_id}")
    else:
        print(f"❌ Không tìm thấy nhắc việc với ID: {reminder_id}")

if __name__ == '__main__':
    # Ví dụ test cập nhật
    updates = {
        "text": "Uống nghệ mật ong + gừng",
        "time": "06:45",
        "repeat_count": 5
    }
    edit_reminder(1, updates)
