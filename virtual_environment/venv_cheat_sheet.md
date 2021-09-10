
### create virtual environment
`python -m venv env/my_virtual_environment`

if you have two versions of python, for example ver 2 and 3, and you want to use version 3.
be specific like this

`python3 -m venv env/my_virtual_environment`


### activate virtual environment
* windows

`C:\Users\artur\git\my_project\env\my_virtual_environment\Scripts\activate.bat`

* linux

`source env/my_virtual_environment/bin/activate`


### deactivate virtual environment windows or linux
`deactivate`


### install libraries in virtual environment
any of these commands


```sh
python -m pip install -r requirements.txt
python -m pip install --requirement requirements.txt
```

### delete virtual environment.

just delete the folder

`rm -fr my_virtual_environment`

---

