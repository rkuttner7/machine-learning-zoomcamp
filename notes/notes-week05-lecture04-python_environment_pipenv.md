# 5.5 Python virtual environment: Pipenv

* Dependency and environment management  
* Why we need virtual environment  
* Installing Pipenv  
* Installing libraries with Pipenv  
* Running things with Pipenv  

### Notes

A virtual environment is an operation that can separate the libraries installed in our system and the libraries with specified version we want our project to run with.

#### Install `pipenv`

Recommended approach is to install Pipenv for your user account. This avoids permission issues and prevents conflicts with system packages:  
```
pip install --user pipenv
```
  
After installing with --user, you may need to add the user site-packages binary directory to your PATH.  
  
Confirm the location user base binary directory is in your home directory:  
```BASH
$ python -m site --user-base
/home/[user-name]/.local
```
  
Add the bin directory to your `PATH` by adding this line to your shell configuration file (e.g., ~/.bashrc, ~/.zshrc, or ~/.profile):  

```BASH
export PATH="$HOME/.local/bin:$PATH"
```
  
Reload your shell configuration:  
```BASH
$ source ~/.bashrc  # or ~/.zshrc, ~/.profile, etc.
```

#### Lock files

Python package dependencies are stored in `Pipfile` and `Pipfile.lock`.


### **Functions and methods:**  

* `pipenv install [python library name] [[== version]]` - install project's python dependcies with pipenv. (**Example**: `pipenv install numpy scikit-learn==1.7.2 flask`)  
    * `pipenv install` will install all libraries tracked in the lock files not yet installed on the current machine.
  
* `pipenv shell` - Activate the environment  

* `pipenv run [command]` - run commands in environment. (shell need not be activated when using command `pipenv`) **Examples**:
    * `pipenv run python [script filename].py`
    * `pipenv run gunicorn --bind 0.0.0.0:9696 predict:app`
  
### **Futher Reading**  
* [Pipenv Best Practices | official documentation](https://pipenv.pypa.io/en/latest/best_practices.html) outlines recommended best practices for using Pipenv effectively in Python projects.  
* [Migrating from Conda to Pipenv | official documentation](https://pipenv.pypa.io/en/latest/migrating.html#migrating-from-conda) steps on extracting Python packages from Conda and identifying non-Python dependencies that Pipenv can’t handle.   
* [Getting started with Poetry | official documentation](https://python-poetry.org/docs/basic-usage/) a more modern Python dependency managment package.  
