from flask import render_template
from app import app

@app.route('/')
def index():
  # return '<h1>Sample App</h1><h2>Welcome</h2>'
  return render_template('page.html', title='Welcome')


@app.route('/help')
def help():
  # return '<h1>Sample App</h1><h2>Help</h2>'
  return render_template('page.html', title='Help')


@app.route('/item/<int:id>')
def item(id):
  if (id > 0 and id < 100):
    item = {
      "id": id,
      "name": f"Fancy Item {id}",
      "description": "Coming soon...",
    }
    # return f'<h1>Sample App</h1><h2>Item {id}</h2>'
    return render_template('item.html', item=item)
  else:
    return '<h1>Sample App</h1><h2>Item Not Found</h2>'


