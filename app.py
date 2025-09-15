from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")   # login page

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # TODO: Save user data in DB
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/teacher/dashboard")
def teacher_dashboard():
    # TODO: fetch teacher + attendance data from DB
    teacher = {"name": "Mr. Sharma", "email": "sharma@example.com"}
    attendance = [
        {"student_name": "Ravi", "date": "2025-09-09", "status": "Present"},
        {"student_name": "Neha", "date": "2025-09-09", "status": "Absent"}
    ]
    return render_template("teacher_dashboard.html", teacher=teacher, attendance=attendance)

@app.route("/student/dashboard")
def student_dashboard():
    # TODO: fetch student data from DB
    student = {"name": "Kasak", "email": "kasak@example.com"}
    attendance = [
        {"date": "2025-09-09", "status": "Present"},
        {"date": "2025-09-08", "status": "Absent"}
    ]
    return render_template("student_dashboard.html", student=student, attendance=attendance)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    # TODO: fetch user data from DB
    user = {"name": "Kasak", "email": "kasak@example.com"}
    if request.method == "POST":
        # TODO: update user data
        return redirect(url_for("profile"))
    return render_template("profile.html", user=user)

@app.route("/attendance")
def attendance():
    attendance = [
        {"student_name": "Ravi", "date": "2025-09-09", "status": "Present"},
        {"student_name": "Neha", "date": "2025-09-09", "status": "Absent"}
    ]
    return render_template("attendance.html", attendance=attendance)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
