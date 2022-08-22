


from flask import Flask, jsonify
from nba_api.stats.static import teams
import os

app = Flask(__name__)

@app.route("/teams")
def get_teams():
    all_teams = teams.get_teams()
    return jsonify(all_teams)



@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
