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


# 📁 delete_reminder.py


# 📁 edit_reminder.py


# 📁 list_reminders.py


# 📁 reminder_manager.py
# Giao diện quản lý toàn bộ nhắc việc: thêm, sửa, xoá, liệt kê
import os
from add_reminder import add_reminder_from_text
from delete_reminder import delete_by_id, delete_by_keyword
from edit_reminder import edit_reminder
from list_reminders import list_reminders

MENU = """
===== 📋 TRỢ LÝ NHẮC VIỆC SẦM BOT =====
1. Xem danh sách nhắc việc
2. Thêm nhắc việc (tiếng Việt tự nhiên)
3. Sửa nhắc việc (theo ID)
4. Xoá nhắc việc (theo ID)
5. Xoá nhắc việc (theo từ khoá)
0. Thoát
"""

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(MENU)
        choice = input("👉 Chọn chức năng (0–5): ").strip()

        if choice == '1':
            list_reminders()
            input("\nNhấn Enter để quay lại...")

        elif choice == '2':
            text = input("Nhập câu nhắc việc bằng tiếng Việt: ")
            result = add_reminder_from_text(text)
            print("✅ Đã thêm:", result)
            input("\nNhấn Enter để quay lại...")

        elif choice == '3':
            rid = int(input("Nhập ID nhắc việc cần sửa: "))
            field = input("Trường cần sửa (text, time, repeat, repeat_count, expires, status): ")
            value = input("Giá trị mới: ")
            if field in ['repeat_count']:
                value = int(value)
            elif value.lower() == 'null':
                value = None
            edit_reminder(rid, {field: value})
            input("\nNhấn Enter để quay lại...")

        elif choice == '4':
            rid = int(input("Nhập ID nhắc việc cần xoá: "))
            delete_by_id(rid)
            input("\nNhấn Enter để quay lại...")

        elif choice == '5':
            keyword = input("Nhập từ khoá cần xoá: ")
            delete_by_keyword(keyword)
            input("\nNhấn Enter để quay lại...")

        elif choice == '0':
            print("👋 Tạm biệt Sầm!")
            break
        else:
            input("❗️ Lựa chọn không hợp lệ. Nhấn Enter để thử lại...")

if __name__ == '__main__':
    main()
