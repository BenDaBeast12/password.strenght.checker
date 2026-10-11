from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    strength = ""
    feedback = ""

    if request.method == "POST":
        password = request.form.get("password", "")

        score = 0

        if len(password) >= 8:
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"
            feedback = "Add length and a mix of character types."
        elif score <= 4:
            strength = "Medium"
            feedback = "Consider using a longer, more varied password."
        else:
            strength = "Strong"
            feedback = "Good mix of length and character types."

    return render_template(
        "index.html",
        strength=strength,
        feedback=feedback
    )


if __name__ == "__main__":
    app.run(debug=True)
