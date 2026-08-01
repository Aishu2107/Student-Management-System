from flask import Flask, render_template, request

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]
        department = request.form["department"]

        students.append({
            "name": name,
            "roll": roll,
            "department": department
        })

        return "Student Saved Successfully!"

    return render_template("add_student.html")

@app.route("/students")
def view_students():
    return render_template("view_students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)