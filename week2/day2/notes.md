# Decorators  
- fxs that take in another fx as an arg (callback)
- fx that wraps an inner fx (closure)
- dynamically modify behavior
- extend wrapped fx's behavior without direct modification
    - doesn't directly modify the original input fx (wtf does this mean)  

## Decorator Syntactic Sugar  
- With syntactic sugar
```python
def my_decorator(fx_to_decorate):
  def my_wrapper_fx():
    print('Hi, I\'m a wrapper!')
    return fx_to_decorate()
  return my_wrapper_fx

@my_decorator
def my_fx_to_decorate():
  print("I\'m a fx to decorate!")
```

- Without syntactic sugar
```python
def my_decorator(fx_to_decorate):
  def my_wrapper_fx():
    print('Hi, I\'m a wrapper!')
    return fx_to_decorate()
  return my_wrapper_fx

def my_fx_to_decorate():
  print("I\'m a fx to decorate!")

fx_to_decorate = my_decorator(fx_to_decorate)
```

# Flask 
- flask is a plugin, extension, library, add-on whatever for Python  
- allows you to specify a path to your browser and return content for it  



# Calendar This 
**Environment Settings**
- `.flaskenv` 
  - you should put the settings in `.flaskenv` that won't change between development and production environments
  - this includes settings like `FLASK_APP` (the entry point for your app)
- `.env`
  - you should put development settings in `.env` because this one won't get checked into source control
  - this should include `FLASK_ENV` and `SECRET_KEY`
