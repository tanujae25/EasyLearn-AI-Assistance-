from flask import Flask, request, render_template
from quiz_generator import generate_quiz

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    quiz = ""
    if request.method == "POST":
        topic = request.form["topic"]
        quiz = generate_quiz(topic)
    return render_template("index.html", quiz=quiz)

if __name__ == "__main__":
    app.run(debug=True)
