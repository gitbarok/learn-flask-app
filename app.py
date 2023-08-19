from flask import Flask, redirect, render_template, request, url_for
from forms import LoginForm, RegistrationForm

# from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "rahasia"

data_dosen = {
    1: {"Nama": "John Doe", "NIP": "1234", "Status": "Available"},
    2: {"Nama": "John Doe", "NIP": "1", "Status": "Available"},
    3: {"Nama": "John Doe", "NIP": "2", "Status": "Not Available"},
    4: {"Nama": "John Doe", "NIP": "13", "Status": "Not Available"},
}


@app.route("/")
def home():
    return render_template("home.html", title="Home", data_dosen=data_dosen)


@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    return render_template("dashboard.html", data_dosen=data_dosen, title="Dashboard")


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    form = RegistrationForm()
    if form.is_submitted():
        new_data = {
            "Nama": form.username.data,
            "NIP": form.password.data,
            "Status": "Available",
        }
        next_key = max(data_dosen.keys(), default=1) + 1
        data_dosen[next_key] = new_data
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
