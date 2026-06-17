from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")


# -------------------------
# REGISTER PAGE
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    account_no = None
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ✅ Generate ONLY 12-digit account number
        account_no = str(random.randint(10**11, 10**12 - 1))

        # ✅ CONDITION: must be exactly 12 digits
        if len(account_no) == 12 and account_no.isdigit():
            message = "Account Created Successfully!"
        else:
            message = "Error: Invalid Account Number"

        return render_template(
            "register.html",
            username=username,
            account_no=account_no,
            message=message
        )

    return render_template("register.html")


# -------------------------
# LOGIN PAGE
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Dummy check (replace with database later)
        if username == "admin" and password == "1234":
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    return redirect(url_for("login"))


# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)