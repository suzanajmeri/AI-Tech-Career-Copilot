# app.py file

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Ensure backend.py is in the same directory
from backend import get_careers, get_roadmap, explore_skill, process_chat

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# ----- Pages -----
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommender")
def recommender_page():
    return render_template("recommender.html")

@app.route("/explorer")
def explorer_page():
    return render_template("explorer.html")

@app.route("/roadmap")
def roadmap_page():
    return render_template("roadmap.html")

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

# ----- APIs -----
@app.route("/api/recommend", methods=["POST"])
def api_recommend():
    data = request.get_json(silent=True) or {}
    skills = data.get("skills", "")
    careers = get_careers(skills)
    return jsonify({"careers": careers})

@app.route("/api/roadmap", methods=["POST"])
def api_roadmap():
    data = request.get_json(silent=True) or {}
    career = data.get("career", "")
    steps = get_roadmap(career)
    return jsonify({"steps": steps})

@app.route("/api/explore", methods=["POST"])
def api_explore():
    data = request.get_json(silent=True) or {}
    skill = data.get("skill", "")
    result = explore_skill(skill)
    resources = [{"title": n, "url": u} for (n, u) in result.get("resources", [])]
    return jsonify({"careers": result.get("careers", []), "resources": resources})

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    reply = process_chat(message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)