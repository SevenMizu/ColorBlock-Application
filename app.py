from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route("/party/<theme>")
def rsvp():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        guests = request.form.get("guests")
        # Process the RSVP details here (e.g., save to a database or file)
        return render_template("thank_you.html", name=name)
    return render_template("rsvp.html")

def party(theme):
    return render_template('party.html', theme=theme)f

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # run our flask app

