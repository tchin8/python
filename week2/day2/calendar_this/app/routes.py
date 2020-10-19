from flask import Blueprint, render_template

bp = Blueprint("main", __name__, "")

@bp.route("/")
def main():
  # return "<h2>Calendar working</h2>"
  return render_template('main.html')

