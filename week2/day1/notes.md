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


# Pip, Virtualenv, and Pipenv  
- used to manage dependencies within app  

**Python tool - Node.js equivalent**   
`pyenv` - `nvm`  
`pip` - `npm --global`  
`virtualenv` - `nvm + node_modules`  
`pipenv` - `npm + nvm`  
`Pipfile` - `package.json`  


# pipenv setup
`export PIPENV_VENV_IN_PROJECT=1`  
`export PYENV_ROOT=$HOME/.pyenv`  
`export PIPENV_PYTHON=$PYENV_ROOT/shims/python`  
`export PATH="$PYENV_ROOT/shims:$PATH"`  

The first line tells pipenv to always put the packages in the local directory of the project rather than in a global directory.

The second line sets the path to your pyenv directory so that pipenv can find it.

The third line tells pipenv to, by default, use the Python currently activated by pyenv.

The fourth line adds the shims directory in your pyenv installation to the search path so that pipenv can tell virtualenv what Python to actually run for the project managed by pipenv.


<!-- !! Not sure if pipenv / pip is set up correctly !! -->


