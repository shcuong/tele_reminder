import json

def delete_by_id(reminder_id):
    with open("reminder.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    new_data = [r for r in data if r.get("id") != reminder_id]

    with open("reminder.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

def delete_by_keyword(keyword):
    with open("reminder.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    new_data = [r for r in data if keyword.lower() not in r.get("text", "").lower()]

    with open("reminder.json", "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)
