from add_reminder import add_reminder_from_text
from delete_reminder import delete_by_id
from edit_reminder import edit_reminder
from list_reminders import load_reminders

def main():
    while True:
        print("\n🎛 MENU:")
        print("1. Thêm nhắc việc")
        print("2. Xoá nhắc việc")
        print("3. Sửa nhắc việc")
        print("4. Xem danh sách")
        print("5. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            text = input("Nhập nội dung: ")
            add_reminder_from_text(text)

        elif choice == "2":
            try:
                rid = int(input("Nhập ID: "))
                delete_by_id(rid)
            except:
                print("ID không hợp lệ.")

        elif choice == "3":
            try:
                rid = int(input("ID cần sửa: "))
                field = input("Trường cần sửa (text, time, repeat...): ")
                value = input("Giá trị mới: ")
                if value.lower() == "none":
                    value = None
                edit_reminder(rid, {field: value})
            except:
                print("Dữ liệu không hợp lệ.")

        elif choice == "4":
            for r in load_reminders():
                print(r)

        elif choice == "5":
            break

        else:
            print("Không hợp lệ!")

if __name__ == "__main__":
    main()
