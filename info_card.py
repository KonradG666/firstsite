from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    data = ["email: konrad@interia.pl" , "phone: 555 666 777", "city: Sosnowiec"]
    return render_template("contact.html", items=data)


@app.route("/submit")
def submit():
    return render_template("contact_form.html")
