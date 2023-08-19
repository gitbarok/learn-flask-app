from flask import Flask, redirect, render_template, request, url_for
from forms import LoginForm, RegistrationForm
import json

# from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "rahasia"

with open("data_dosen.json", "r") as json_file:
    data_dosen = json.load(json_file)


@app.route("/")
def home():
    with open("data_dosen.json", "r") as json_file:
        data_dosen = json.load(json_file)
    return render_template("home.html", title="Home", data_dosen=data_dosen)


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    with open("data_dosen.json", "r") as json_file:
        data_dosen = json.load(json_file)
    return render_template("dashboard.html", data_dosen=data_dosen, title="Dashboard")


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    form = RegistrationForm()
    with open("data_dosen.json", "r") as json_file:
        data_dosen = json.load(json_file)
    if form.is_submitted():
        new_data = {
            "Nama": form.username.data,
            "NIP": form.password.data,
            "Status": "Available",
        }
        next_key = str(max(map(int, data_dosen.keys()), default=0) + 1)
        data_dosen[next_key] = new_data

        with open("data_dosen.json", "w") as json_file:
            json.dump(data_dosen, json_file, indent=4)

        return redirect(url_for("dashboard"))
    return render_template("add_user.html", form=form, title="add user")


@app.route("/dashboard/<int:key>/delete", methods=["POST"])
def delete_user(key):
    data_dosen.pop(key)
    return redirect(url_for("dashboard"))


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.is_submitted():
        if form.username.data == "anjay" and form.password.data == "password":
            return redirect(url_for("dashboard"))
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
