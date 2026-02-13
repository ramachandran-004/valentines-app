from flask import Flask, render_template_string, request
import random
app = Flask(__name__)
app.secret_key = "secret_key"
HER_NAME= "Hebah"
messages= [
    'I really love how pretty your eyes are',
    'Whenever you smile, it just makes my day a thousand times better',
    'I love the way you play with my hair, it makes me feel so special',
    'You never stop making me laugh, you just don\'t stop making me smile',
    'I love the fact that you can clock me at any given point of time and that you just understand me so well',
    'You are literally the nicest person I have ever met, you are so kind and caring',
    'I can never stop taking a whiff of your hair, it is literally COCAINE',
    'I love it when you talk about things you are passionate about, it just makes me love you more',
    'I love how you are so good at cooking, it just makes me want to eat you up',
    'I can not sleep without having you stay on call with me, I just can\'t sleep without hearing your voice',
]
@app.route('/')
def home():
    index = request.args.get("index", 0)
    index = int(index)

    if index < len(messages):
        message = messages[index]
        next_index = index + 1

        button_html = f"""
        <form method="get">
            <input type="hidden" name="index" value="{next_index}">
            <button type="submit">Next ❤️</button>
        </form>
        """
    else:
        message = "❤️ Happy Valentine’s Day Hebah ❤️"
        button_html = """
        <form method="get">
            <input type="hidden" name="index" value="0">
            <button type="submit">Start Again 💕</button>
        </form>
        """
    return f"""
    <html>
    <head>
        <title>For {HER_NAME}</title>
        <style>
            body {{
                font-family: Arial;
                background: #fff8f0;
                text-align: center;
                padding-top: 80px;
                overflow: hidden;
            }}
            .card {{
                background: white;
                display: inline-block;
                padding: 35px;
                border-radius: 18px;
                box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
                font-size: 18px;
                max-width: 420px;
                position: relative;
                z-index: 2;
            }}
            button {{
                margin-top: 25px;
                padding: 10px 22px;
                border: none;
                border-radius: 10px;
                background-color: #ffb6b9;
                cursor: pointer;
                font-size: 15px;
            }}
            .heart {{
                position: absolute;
                bottom: -20px;
                font-size: 18px;
                animation: floatUp 6s linear infinite;
                opacity: 0.6;
            }}
            @keyframes floatUp {{
                0% {{ transform: translateY(0); opacity: 0.8; }}
                100% {{ transform: translateY(-700px); opacity: 0; }}
            }}
        </style>
    </head>
    <body>

        <div class="card">
            <h2>For {HER_NAME} 💛</h2>
            <p style="font-size:20px;">{message}</p>
            {button_html}
        </div>

        <script>
            function createHeart() {{
                const heart = document.createElement("div");
                heart.classList.add("heart");
                heart.innerHTML = "🤍";
                heart.style.left = Math.random() * 100 + "vw";
                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), 6000);
            }}
            setInterval(createHeart, 500);
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
