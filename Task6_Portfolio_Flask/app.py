from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]

    return f"""
    <html>
    <body style="background: linear-gradient(135deg, #667eea, #764ba2); font-family: Arial; text-align: center; padding-top: 100px;">
        <div style="background: white; padding: 40px; border-radius: 15px; width: 50%; margin: auto;">
            <h1 style="color: green;">Thank You {name}!</h1>
            <p>Your message has been received successfully.</p>
            <a href="/" style="background: #6c5ce7; color: white; padding: 10px 20px; text-decoration: none; border-radius: 8px;">Back to Portfolio</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)