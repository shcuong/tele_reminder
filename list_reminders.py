import json

def load_reminders():
    with open("reminder.json", "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    reminders = load_reminders()
    for r in reminders:
        print(f"ID: {r['id']} | {r['text']} | {r['time']} | {r.get('repeat')} | {r.get('status')}")
