from datetime import datetime, timedelta
from flask import Blueprint, render_template, redirect, url_for
from .forms import AppointmentForm
import os
import psycopg2

bp = Blueprint("main", __name__, "")

CONNECTION_PARAMETERS = {
  "user": os.environ.get("DB_USER"),
  "password": os.environ.get("DB_PASS"),
  "dbname": os.environ.get("DB_NAME"),
  "host": os.environ.get("DB_HOST"),
}

@bp.route("/")
def main():
  d = datetime.now()
  return redirect(url_for(".daily", year=d.year, month=d.month, day=d.day))


@bp.route("/<int:year>/<int:month>/<int:day>", methods=["GET", "POST"])
# def main():
#   # return "<h2>Calendar working</h2>"
#   return render_template('main.html')
def daily(year, month, day):
  form = AppointmentForm()
  if form.validate_on_submit():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
      with conn.cursor() as curs:
        sql = """
          INSERT INTO appointments (
            name,
            start_datetime,
            end_datetime,
            description,
            private
          )
          VALUES
          (
            %(name)s,
            %(start_datetime)s,
            %(end_datetime)s,
            %(description)s,
            %(private)s
          )
        """
      params = {
        'name': form.name.data,
        'start_datetime': datetime.combine(
                          form.start_date.data,
                          form.start_time.data,
                          ),
        'end_datetime': datetime.combine(
                          form.end_date.data,
                          form.end_time.data,
                        ),
        'description': form.description.data,
        'private': form.private.data
      }
      curs.execute(sql, params)
      return redirect("/")
  with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
      day = datetime(year, month, day)
      next_day = day + timedelta(days=1)
      sql = """
        SELECT id, name, start_datetime, end_datetime
        FROM appointments
        WHERE start_datetime BETWEEN %(day)s AND %(next_day)s
        ORDER BY start_datetime
      """
      curs.execute(sql, {'day': day, 'next_day': next_day})
      rows = curs.fetchall()
      return render_template("main.html", rows=rows, form=form)
