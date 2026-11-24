# web_app/routes/rps_routes.py
from random import choice
from flask import Blueprint, request, render_template

from app.rps import determine_winner, VALID_OPTIONS

rps_routes = Blueprint("rps_routes", __name__)

@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html")

@rps_routes.route("/rps/play", methods=["GET", "POST"])
def rps_play():
    print("RPS PLAY...")

    # the form sends its data here when the user clicks "Play"
    if request.method == "POST":
        data = dict(request.form)
    else:
        data = dict(request.args)
    print("FORM DATA:", data)

    user_choice = data.get("user_choice") or "rock"
    computer_choice = choice(VALID_OPTIONS)
    winner = determine_winner(user_choice, computer_choice)

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner
    )
