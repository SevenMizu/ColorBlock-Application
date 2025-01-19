from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route("/party/<theme>")
def party(theme):
    return render_template('party.html', theme=theme)

if __name__ == '__main__':
    app.run(debug=True)

