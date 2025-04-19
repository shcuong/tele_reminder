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
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 reminder_parser.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 add_reminder.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 delete_reminder.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 edit_reminder.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 list_reminders.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 reminder_manager.py
# <... (không đổi - giữ nguyên như trước) ...>

# 📁 reminder_web.py
from flask import Flask, request, render_template_string, redirect, jsonify
from add_reminder import add_reminder_from_text
from delete_reminder import delete_by_id
from edit_reminder import edit_reminder
from list_reminders import load_reminders

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Trợ lý nhắc việc SầmBot</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        td, th { border: 1px solid #ccc; padding: 8px; }
        th { background-color: #f4f4f4; }
        input[type=text], input[type=number] { width: 100%; }
    </style>
</head>
<body>
    <h2>📋 Danh sách nhắc việc</h2>
    <form method="post" action="/add">
        <input type="text" name="text" placeholder="Nhập nhắc việc bằng tiếng Việt...">
        <button type="submit">➕ Thêm</button>
    </form>
    <br>
    <form method="get" action="/">
        <label>Lọc theo trạng thái: </label>
        <select name="status">
            <option value="">-- Tất cả --</option>
            <option value="active">Đang hoạt động</option>
            <option value="done">Đã hoàn thành</option>
        </select>
        <button type="submit">Lọc</button>
    </form>
    <br>
    <table>
        <tr><th>ID</th><th>Nội dung</th><th>Giờ</th><th>Lặp</th><th>Ngày</th><th>Lần</th><th>Hết hạn</th><th>Trạng thái</th><th>Hành động</th></tr>
        {% for r in reminders %}
        <tr>
            <form method="post" action="/edit">
                <td>{{ r.id }}<input type="hidden" name="id" value="{{ r.id }}"></td>
                <td><input type="text" name="text" value="{{ r.text }}"></td>
                <td><input type="text" name="time" value="{{ r.time }}"></td>
                <td><input type="text" name="repeat" value="{{ r.repeat }}"></td>
                <td><input type="text" name="days_of_week" value="{{ r.days_of_week|join(',') if r.days_of_week }}"></td>
                <td><input type="text" name="repeat_count" value="{{ r.repeat_count or '' }}"></td>
                <td><input type="text" name="expires" value="{{ r.expires or '' }}"></td>
                <td><input type="text" name="status" value="{{ r.status }}"></td>
                <td>
                    <button type="submit">💾</button>
                    <form method="post" action="/delete" style="display:inline;">
                        <input type="hidden" name="id" value="{{ r.id }}">
                        <button type="submit">🗑</button>
                    </form>
                </td>
            </form>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    status_filter = request.args.get('status')
    data = load_reminders()
    if status_filter:
        data = [r for r in data if r.get('status') == status_filter]
    return render_template_string(TEMPLATE, reminders=data)

@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('text')
    if text:
        add_reminder_from_text(text)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    rid = int(request.form.get('id'))
    delete_by_id(rid)
    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit():
    rid = int(request.form.get('id'))
    updates = {
        "text": request.form.get("text"),
        "time": request.form.get("time"),
        "repeat": request.form.get("repeat"),
        "days_of_week": [s.strip() for s in request.form.get("days_of_week", "").split(",") if s.strip()],
        "repeat_count": int(request.form.get("repeat_count")) if request.form.get("repeat_count") else None,
        "expires": request.form.get("expires") or None,
        "status": request.form.get("status")
    }
    edit_reminder(rid, updates)
    return redirect('/')

@app.route('/api/reminders', methods=['GET'])
def api_reminders():
    return jsonify(load_reminders())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
