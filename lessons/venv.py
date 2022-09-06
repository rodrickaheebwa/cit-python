# create a python virtual environment before downloading modules; in case projects differ in the versions of a module they will use.
# venv - tool used to create the environment
# python[python version to use] -m venv[tool] venv[name]
# python -m venv venv
# .\venv\Scripts\activate
# the virtual environment is created in that project folder
# seperate the dependencies of one project from the dependencies of another
# the python version and module versions can't be changed there after
# changes path so that the COPY of python run by the venv is the first on the list of paths
# the pip run from the environment will also be different (one that comes with the venv)
# all modules installed by pip will be in this venv