import json
from reminder_parser import parse_reminder

def add_reminder_from_text(text):
    try:
        with open("reminder.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    new_id = max([r["id"] for r in data], default=0) + 1
    parsed = parse_reminder(text)

    reminder = {
        "id": new_id,
        "text": parsed.get("text", text),
        "time": parsed.get("time"),
        "repeat": parsed.get("repeat"),
        "days_of_week": parsed.get("days_of_week"),
        "repeat_count": parsed.get("repeat_count"),
        "expires": parsed.get("expires"),
        "status": "active"
    }

    data.append(reminder)

    with open("reminder.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
