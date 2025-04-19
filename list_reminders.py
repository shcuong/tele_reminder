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
<... (không đổi - giữ nguyên như trước) ...>

# 📁 list_reminders.py
# Hiển thị danh sách các nhắc việc hiện có
import json
from tabulate import tabulate

REMINDER_FILE = 'reminder.json'

def load_reminders():
    with open(REMINDER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def list_reminders():
    reminders = load_reminders()
    if not reminders:
        print("📭 Không có nhắc việc nào.")
        return

    table = []
    for r in reminders:
        table.append([
            r.get("id"),
            r.get("text"),
            r.get("time"),
            r.get("repeat"),
            ", ".join(r["days_of_week"]) if r.get("days_of_week") else "",
            r.get("repeat_count", ""),
            r.get("expires", ""),
            r.get("status")
        ])

    headers = ["ID", "Nội dung", "Giờ", "Lặp", "Ngày cụ thể", "Số lần", "Hết hạn", "Trạng thái"]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

if __name__ == '__main__':
    list_reminders()
