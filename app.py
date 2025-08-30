from flask import Flask, render_template, request
import os
from categorizer import categorize_expenses

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df, summary = categorize_expenses(filepath)
            if df is None:
                return f"Error: {summary}"

            return render_template(
                "index.html",
                tables=[df.to_html(classes='data', header="true", index=False)],
                summary=summary
            )
        else:
            return "Please upload a CSV file with '.csv' extension."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
