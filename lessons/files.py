# open
# perform operations
# close
# use try, finally - to open and close
# or with open

"""
os.getcwd() - get current working directory
os.chdir() - change working directory
os.makedirs() - create new directories
os.path.join() - joins string arguments to form a path
os.path.abspath(path) - gets absolute path of relative path
os.path.isabs(path) - checks if path is absolute
os.path.relpath(path, start) - returns a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path
os.path.dirname(path) - everything that comes before the last slash in the path argument
os.path.basename(path) - everything that comes after the last slash in the path argument
os.path.split(path) - splits dirname and basename into a tuple
path.split(os.path.sep) - returns list of folders in path / opposite of join()
os.path.getsize(path) - gets size in bytes of a file
os.path.exists() - checks if a path exists
os.path.isfile() - checks if the path exists and if its a file
os.path.isdir()
os.walk() - handles trek across folder tree

os module works on manipulating plain text files.
For binary files, there exists modules like shelve.

The shelve module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.

Plaintext is useful for creating files that you will read in a text editor such as Notepad or TextEdit, but if you want to save data from your Python programs, use the shelve module.

Using pprint.pformat() can help you generate python files using python code.
"""