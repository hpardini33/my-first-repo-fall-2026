# web_app/routes/stocks_routes.py
from flask import Blueprint, request, render_template, redirect

from app.stocks import fetch_stocks_data, format_usd

stocks_routes = Blueprint("stocks_routes", __name__)

@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html")

@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        request_data = dict(request.form)
    else:
        request_data = dict(request.args)
    print("REQUEST DATA:", request_data)

    symbol = (request_data.get("symbol") or "NFLX").upper()

    try:
        df = fetch_stocks_data(symbol=symbol)
        latest_close_usd = format_usd(df.iloc[0]["close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        return render_template("stocks_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            data=data
        )
    except Exception as err:
        print("OOPS", err)
        return redirect("/stocks/form")