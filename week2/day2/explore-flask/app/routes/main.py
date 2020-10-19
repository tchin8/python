from flask import Blueprint, render_template, redirect, session
from app.forms.login import LoginForm

bp = Blueprint('', __name__)


def track_views():
  if 'views' in session:
    session['views'] = session.get('views') + 1
  else:
    session['views'] = 1


@bp.route('/')
def index():
  # return '<h1>Sample App</h1><h2>Welcome</h2>'
  track_views()
  return render_template('page.html', title='Welcome')


@bp.route('/views')
def views():
  return f'Total views: {session.get("views")}'


@bp.route('/views/reset')
def reset_views():
  views = session.pop('views', None)  
  return f'Reset views (previous {views})'


@bp.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    # return redirect('/')
    return 'Submit complete'
  return render_template('login.html', form=form)


@bp.route('/help')
def help():
  # return '<h1>Sample App</h1><h2>Help</h2>'
  track_views()
  return render_template('page.html', title='Help')
