from flask import Blueprint, render_template
import psycopg2
import os

bp = Blueprint("main", __name__, "")

CONNECTION_PARAMETERS = {
  "user": os.environ.get("DB_USER"),
  "password": os.environ.get("DB_PASS"),
  "dbname": os.environ.get("DB_NAME"),
  "host": os.environ.get("DB_HOST"),
}

@bp.route("/")
# def main():
#   # return "<h2>Calendar working</h2>"
#   return render_template('main.html')
def main():
  with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
      curs.execute("""
                  SELECT id, name, start_datetime, end_datetime
                  FROM appointments
                  ORDER BY start_datetime;
                  """)
      rows = curs.fetchall()
      return render_template("main.html", rows=rows)
