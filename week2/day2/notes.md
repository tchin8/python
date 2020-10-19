# Decorators  
- fxs that take in another fx as an arg (callback)
- fx that wraps an inner fx (closure)
- dynamically modify behavior
- extend wrapped fx's behavior without direct modification
    - doesn't directly modify the original input fx (wtf does this mean)  

```python
def message_decorator(message_func):
  def message_wrapper(name):
    from_statement = 'This is a message from ' + name
    print(message_func() + from_statement)
  return message_wrapper

def say_hi():
  return 'Hi! '

def say_bye():
  return 'Bye! '
```

Note the order of what is happening in the message_decorator function:
1. The decorator function (`message_decorator`) takes in a function to invoke.
2. The inner wrapper function is defined (`message_wrapper`).
3. There is functional code that happens before the decorator's function argument is invoked (`from_statement = ...`).
4. The decorator's function argument is invoked (`message_func()`).
5. The wrapper function is returned (`return message_wrapper`).

```python
def message_decorator(message_func):
  def message_wrapper(name):
    from_statement = 'This is a message from ' + name
    print(message_func() + from_statement)
  return message_wrapper

def say_hi():
  return 'Hi! '

def say_bye():
  return 'Bye! '

print(say_hi)             # <function say_hi at 0x10f1a9280>>
print(say_hi.__closure__) # None

say_hi = message_decorator(say_hi)
print(say_hi)             # <function message_decorator.<locals>.message_wrapper at 0x10f1a93a0>
```



## Callbacks  
- py fxs can be passed as rgs just like callbacks from JS
- py fxs are first-class objects  
  - since they're first-class objects, there are no restrictions to how the fxs can be used (so they can be passed as an arg)  

```python
def say_hi(name):
  print(f'Hi, {name}!')

def say_good_morning(name):
  print(f'Good morning, {name}!')

def say_something_to_curtis(say_something_func):
  return say_something_func('Curtis')

say_something_to_curtis(say_hi)            # Hi, Curtis!
say_something_to_curtis(say_good_morning)  # Good morning, Curtis!
```

## Instrospection
- introspection is the ability to examing objects to determine its behavior or type 
- can use the built-in `dir()` fx to observe the `say_hi` object  

```python
def say_hi(name):
  print(f'Hi, {name}!')

print(say_hi)       # <function say_hi at 0x1037a41f0>
print(dir(say_hi))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

print(say_hi.__closure__) # None
```  

- notice how the fx has `__closure__` attribute

## Inner functions (aka closures)
- a closure is formed when an inner fx is defined within an outer fx so that the inner fx can reference args passed into the outer fx
- this binds the outer args to the inner fx whenever the outer fx is invoked 

```python
def say_hi_to(name):
  def say_from(author):
    print(f'Hi, {name}!')
    print(f'This is a message from {author}.')
  return say_from

say_hi_ryan_from = say_hi_to('Ryan')
say_hi_ryan_from('Julia')             # Hi, Ryan! This is a message from Julia.
say_hi_ryan_from('Erik')              # Hi, Ryan! This is a message from Erik.

print(say_hi_ryan_from.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
print(say_hi_ryan_from.__closure__[0].cell_contents)  # Ryan

say_hi_andrew_from = say_hi_to('Andrew')
say_hi_chris_from = say_hi_to('Chris')
say_hi_andrew_from('Julia')       # Hi, Andrew! This is a message from Julia.
say_hi_chris_from('Julia')        # Hi, Chris! This is a message from Julia.
```


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
