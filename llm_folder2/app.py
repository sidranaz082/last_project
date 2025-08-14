from flask import Flask, render_template, request
from llm_wrapper import generate_resume

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", resume=None)

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    summary = request.form["summary"]
    skills = request.form["skills"]
    experience = request.form["experience"]
    education = request.form["education"]
    template_choice = request.form["template"]

    resume_html = generate_resume(
        name=name,
        email=email,
        phone=phone,
        summary=summary,
        skills=skills,
        experience=experience,
        education=education,
        template_choice=template_choice
    )

    return render_template("index.html", resume=resume_html)

if __name__ == "__main__":
    app.run(debug=True)
