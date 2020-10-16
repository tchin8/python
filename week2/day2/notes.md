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

