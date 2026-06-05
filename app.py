from flask import Flask, request, render_template
from main import analyze_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    score = 0
    findings = []
    url_value = ""

    if request.method == "POST":

        url_value = request.form["url"]

        score, findings = analyze_url(url_value)

        if score >= 50:
            result = "🚨 High Risk Website"

        elif score >= 20:
            result = "⚠️ Medium Risk Website"

        else:
            result = "✅ Low Risk Website"

    return render_template(
        "index.html",
        result=result,
        score=score,
        findings=findings,
        url_value=url_value
    )

if __name__ == "__main__":
    app.run(debug=True)