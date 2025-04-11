from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = 'oracle_secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'secret' not in session:
        session['secret'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ""

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1
        secret = session['secret']

        if guess < secret:
            message = "🧩 Too low. Think higher."
        elif guess > secret:
            message = "🔺 Too high. Seek lower."
        else:
            message = f"✨ Correct! You found it in {session['attempts']} attempts."
            session.pop('secret')
            session.pop('attempts')

    return render_template('index.html', message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)
