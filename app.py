from flask import Flask, request, jsonify, render_template
import openai

# إعداد مفتاح OpenAI API
openai.api_key = "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"  # ضع مفتاح API الخاص بك هنا

# إنشاء تطبيق Flask
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    # جلب رسالة المستخدم من الطلب
    user_message = request.json.get("message")
    try:
        # استدعاء GPT للحصول على الرد
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي."},
                {"role": "user", "content": user_message},
            ],
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
