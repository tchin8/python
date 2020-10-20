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

## Arguments
```python
def message_decorator(message_func):
  def message_wrapper(name, author):
    return f'{message_func(name)}! This is a message from {author}.'
  return message_wrapper

@message_decorator
def say_hi(name):
  return f'Hi, {name}'

print(say_hi('Julia', 'Ryan'))  # Hi, Julia! This is a message from Ryan.
```  

Desctructured positional args using `*args`
```python
def message_decorator(message_func):
  def message_wrapper(*args):
    name, author = args
    message = message_func(name)
    return f'{message}! This is a message from {author}.'
  return message_wrapper

@message_decorator
def say_hi(name):
  return f'Hi, {name}'

print(say_hi('Julia', 'Ryan'))  # Hi, Julia! This is a message from Ryan.
```  

****kwargs**
- keyword args
```python
def message_decorator(message_func):
  def message_wrapper(*args, **kwargs):
    message = message_func(kwargs['name'])
    author = kwargs['author']
    return f'{message}! This is a message from {author}.'
  return message_wrapper

@message_decorator
def say_hi(name):
  return f'Hi, {name}'

print(say_hi(name='Julia', author='Ryan'))  # Hi, Julia! This is a message from Ryan.
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

## Built-in Class Decorators
- python has a few built-in class decorators:
  - `@property`
    - this decorator referenes python's built-in `property()` fx to get a class attribute
    - it can be used to define the getter of a class property
    - the property getter also has associated *setter* and *deleter* methods
  - `@classmethod`
  - `@staicmethod`

```python
class Ring:
  def __init__(self):
    self._nickname = "Shiny ring"

  @property
  def nickname(self):
    return self._nickname

  @nickname.setter
  def nickname(self, value):
    self._nickname = value

  @nickname.deleter
  def nickname(self):
    del self._nickname
    print('Oh no! The ring is gone!')

ring = Ring()
print(ring.nickname)                  # Shiny ring
ring.nickname = "Gollum's precious"
print(ring.nickname)                  # Gollum's precious
del ring.nickname                     # Oh no! The ring is gone!
```

## Custom Class Decorators
- like how you wrote a decorator for a fx outside of a class, you can use decorators to wrap method definitions
- can also write reusable decorators to wrap class definitions and modify the behavior of an entire class
  - can used a class decorate to implement the singleton software design pattern

```python
from functools import wraps

def singleton_decorator(class_definition):
  @wraps(class_definition)
  def class_wrapper():
    if not class_wrapper.instance:
      class_wrapper.instance = class_definition()
    return class_wrapper.instance
  class_wrapper.instance = None
  return class_wrapper
 
@singleton_decorator
class OneRingToRuleThemAll:
  """
  This is a class for The Ring from Lord of the Rings.
  """
  def __init__(self):
    self._nickname = "Gollum's precious"
 
first_ring = OneRingToRuleThemAll()
second_ring = OneRingToRuleThemAll()
third_ring = OneRingToRuleThemAll()
print(first_ring)   # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
print(second_ring)  # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
print(third_ring)   # <__main__.OneRingToRuleThemAll object at 0x1023981f0>
print(OneRingToRuleThemAll.__name__)  # OneRingToRuleThemAll
print(OneRingToRuleThemAll.__doc__)   # This is a class for The Ring from Lord of the Rings.
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

## Psycopg w/ Postgres
1. open sql shell 
  - `psql -U`
    - `\l` to list all db's
2. create user, pw
  - obviously, don't use 'password'
    ```sql
    CREATE USER calendar_this WITH CREATEDB PASSWORD 'password';
    ```
3. create db
    ```sql
    CREATE DATABASE calendar_this_dev WITH OWNER calendar_this;
    ```
4. create table
    ```sql
    CREATE TABLE appointments (
      id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      start_datetime TIMESTAMP NOT NULL,
      end_datetime TIMESTAMP NOT NULL,
      description TEXT NOT NULL,
      private BOOLEAN NOT NULL
    );
    ```
5. checkkk it outtt, put one record in there
    ```sql
    INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
    VALUES
    ('My appointment', '2020-10-19 14:00:00', '2020-10-19 15:00:00',
    'An appointment for me', false);
    ```
6. put connect URL into the `.env` file
    ```python
    DB_USER=calendar_this
    DB_PASS=password
    DB_NAME=calendar_this_dev
    DB_HOST=localhost
    ```

## *Errors*  
`InsufficientPrivilege: permission denied for table appointments`  
Fixed it with this link:  
https://www.codegrepper.com/code-examples/sql/postgresql+Insufficient+privilege%3A+7+ERROR%3A+permission+denied+for+table  

- One Table 
  - I ran this one specifically. this took me forever to fix. was so annoying. WHY EVEN HAVE THIS HAPPEN?  
  - `GRANT ALL PRIVILEGES ON TABLE appointments TO <user>;` 

- All Tables of schema  
  - `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO <user>;`  
