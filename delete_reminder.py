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
# Xoá nhắc việc theo ID hoặc từ khoá tìm thấy trong nội dung nhắc
import json

REMINDER_FILE = 'reminder.json'

def load_reminders():
    with open(REMINDER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(reminders, f, indent=2, ensure_ascii=False)

def delete_by_id(reminder_id):
    reminders = load_reminders()
    new_list = [r for r in reminders if r['id'] != reminder_id]
    if len(new_list) == len(reminders):
        print(f"❌ Không tìm thấy nhắc việc với ID: {reminder_id}")
    else:
        save_reminders(new_list)
        print(f"✅ Đã xoá nhắc việc có ID: {reminder_id}")

def delete_by_keyword(keyword):
    reminders = load_reminders()
    new_list = [r for r in reminders if keyword.lower() not in r['text'].lower()]
    removed = len(reminders) - len(new_list)
    if removed == 0:
        print(f"❌ Không tìm thấy nhắc việc chứa từ khoá: '{keyword}'")
    else:
        save_reminders(new_list)
        print(f"✅ Đã xoá {removed} nhắc việc chứa từ khoá: '{keyword}'")

if __name__ == '__main__':
    # Ví dụ test xóa
    delete_by_id(2)
    # delete_by_keyword("nghệ")
