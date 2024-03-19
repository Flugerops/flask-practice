from .. import app
from flask import render_template


players = [

    {"name": "Player1", "id": 1, "matches": 10, "goals": 5, "wins": 6, "winrate": 20},

    {"name": "Player2", "id": 2, "matches": 15, "goals": 8, "wins": 10, "winrate": 30},

    {"name": "Player3", "id": 3, "matches": 8, "goals": 3, "wins": 5, "winrate": 50},

    {"name": "Player4", "id": 4, "matches": 12, "goals": 7, "wins": 9, "winrate": 60},

]

@app.route("/")
def index():    
    return render_template("_base.html")

@app.route("/players")
def players_stats():
    players = [

    {"name": "Player1", "matches": 10},

    {"name": "Player2", "matches": 15},

    {"name": "Player3", "matches": 12},

    {"name": "Player4", "matches": 8},

    ]

    return render_template("players.html", players=players)

@app.route("/statistics/<int:player_id>", methods=["GET"])
def stats(player_id):
    for player in players:
        if player["id"] == player_id:
            winrate = player["wins"] / player["matches"]
            return render_template("stats.html", player=player, winrate=winrate)