import json

def edit_reminder(reminder_id, updates):
    with open("reminder.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for r in data:
        if r.get("id") == reminder_id:
            r.update(updates)
            break

    with open("reminder.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
