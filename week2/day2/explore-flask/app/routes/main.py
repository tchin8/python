from flask import Blueprint, render_template, redirect
from app import app

bp = Blueprint('', __name__)

@bp.route('/')
def index():
  # return '<h1>Sample App</h1><h2>Welcome</h2>'
  return render_template('page.html', title='Welcome')

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#   form = LoginForm()
#   if form.validate_on_submit():
#     return redirect('/')
#   return render_template('login.html', form=form)

@bp.route('/help')
def help():
  # return '<h1>Sample App</h1><h2>Help</h2>'
  return render_template('page.html', title='Help')
