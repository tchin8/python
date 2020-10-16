# Modules
## Two Kinds of Modules
  - Directories:  
    - `__init__.py` initializes the directory module when it's imported or ran as a program
    - `__main__.py` runs if it is invoked as a program  

## Files can invoke Modules in two diff ways
  - As a script:
    - `python my_package/my_module.py`
  - As a module:
    - `python -m my_package.my_module`

## Directories can invoke Modules too  
- dirs can be modules too  
- can only invoke modules if dir contains both `__init__.py` file and `__main__.py`  
  - As a script:
    - `python my_package`
  - As a module:
    - `python -m my_package`

