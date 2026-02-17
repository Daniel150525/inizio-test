from flask import Flask, render_template, request
import json

app = Flask(__name__)

def get_results(keyword):
    results = [
        {"title": f"{keyword} - stránka1", "url":"https://example.com/1"},
        {"title": f"{keyword} - stránka2", "url":"https://example.com/2"},
        {"title": f"{keyword} - stránka3", "url":"https://example.com/3"},
    ]
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")

        results = get_results(keyword)

        with open("results.json", "w") as f:
            json.dump(results, f, indent=2)
            
        return f"Uloženo {len(results)} výsledků do results.json"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)