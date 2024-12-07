from flask import Flask, request, render_template, jsonify
import os
import datetime

app = Flask(__name__)

# التأكد من وجود مجلد "submissions" لتخزين البيانات
if not os.path.exists('submissions'):
    os.makedirs('submissions')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # إنشاء محتوى للملف النصي
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"""
📅 **تاريخ الإدخال**: {current_time}
👤 **الاسم**: {name}
📧 **البريد الإلكتروني**: {email}
💬 **الرسالة**:
{message}
---------------------------
"""

        # كتابة البيانات في ملف نصي
        with open('submissions/submission.txt', 'a', encoding='utf-8') as file:
            file.write(content)

        return jsonify({"message": "تم إرسال البيانات بنجاح!"})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
