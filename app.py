import sqlite3
import re
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # user id
        user_id = request.form.get("id")
        if not user_id:
            return redirect("/")
        try:
            user_id = int(user_id)
        except ValueError:
            return redirect("/")

        # name
        name = request.form.get("name")
        if not name:
            return redirect("/")

        # dob (keep as string)
        dob = request.form.get("dob")
        if not dob:
            return redirect("/")

        # email
        email = request.form.get("email")
        if not email:
            return redirect("/")

        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            return redirect("/")

        conn = get_db_connection()
        try:  # this was corrected
            conn.execute(
                "INSERT INTO users (id, name, dob, email) VALUES (?, ?, ?, ?)",
                (user_id, name, dob, email)
            )
            conn.commit()  # this was corrected
        except sqlite3.IntegrityError:  # this was corrected
            pass  # this was corrected
        finally:  # this was corrected
            conn.close()  # this was corrected

        return redirect("/")  # IMPORTANT

    # GET request
    conn = get_db_connection()
    database = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template("index.html", entries=database)  # this was corrected
