


from flask import Flask, jsonify, request
import simplejson

from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import os

app = Flask(__name__)

@app.route("/teams")
def get_teams():
    all_teams = teams.get_teams()
    return jsonify(all_teams)

@app.route("/games")
def get_games():
    team_id = request.args.get('team_id')
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games = gamefinder.get_data_frames()[0]
    return jsonify(simplejson.dumps(games.to_dict('records'), ignore_nan=True))


@app.route('/')
def index():
    return jsonify({"Nba Api": "Welcome to the NBA Api 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
