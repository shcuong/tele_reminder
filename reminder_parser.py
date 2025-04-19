import re
from datetime import datetime
import uuid

VIETDAY = {
    "thứ hai": "monday",
    "thứ ba": "tuesday",
    "thứ tư": "wednesday",
    "thứ năm": "thursday",
    "thứ sáu": "friday",
    "thứ bảy": "saturday",
    "chủ nhật": "sunday"
}

def parse_natural_reminder(text):
    result = {
        "id": int(str(uuid.uuid4().int)[:6]),
        "text": "",
        "time": "",
        "repeat": None,
        "repeat_count": None,
        "expires": None,
        "days_of_week": None,
        "status": "active"
    }

    match_text = re.search(r"nhắc.*?là\s(.+)", text)
    result["text"] = match_text.group(1).strip() if match_text else text.strip()

    match_time = re.search(r"(\d{1,2})[h:](\d{2})", text)
    if match_time:
        hour = match_time.group(1).zfill(2)
        minute = match_time.group(2).zfill(2)
        result["time"] = f"{hour}:{minute}"

    if "mỗi ngày" in text or "hằng ngày" in text:
        result["repeat"] = "daily"
    if "hàng tuần" in text or "mỗi tuần" in text:
        result["repeat"] = "weekly"

    days = [v for k, v in VIETDAY.items() if k in text]
    if days:
        result["repeat"] = "weekly"
        result["days_of_week"] = days

    match_count = re.search(r"(\d+) lần", text)
    if match_count:
        result["repeat_count"] = int(match_count.group(1))

    match_expire = re.search(r"đến ngày (\d{1,2})[/-](\d{1,2})[/-](\d{4})", text)
    if match_expire:
        d, m, y = match_expire.groups()
        result["expires"] = f"{y}-{m.zfill(2)}-{d.zfill(2)}"

    return result
