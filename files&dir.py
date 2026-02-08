#For files and directory path, os.path and pathlib module
# pathlib.Path: cross-platform path handling
#windows - \, macOS, Linux - / use as a path separator
#shutil module provides functions for copying files, as well as entire folders.
from pathlib import Path
import os.path
import shutil
print(Path('usr').joinpath('bin').joinpath('spam'))  # Join path components
print(Path('usr') / 'bin' / 'spam')  # Use / operator instead of joinpath()

# Path.home(): get user's home directory, combine with filenames
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()  # Get home directory path()
print(Path.cwd()) #current working dir
for filename in my_files:
    print(home / filename)  # Combine home path with each filename

# Expand ~ to user's home directory
print(os.path.expanduser('~\Documents'))

#Create new folders,earlier we were getting error because delicious dir was not available, so
#make sure parent folders are available
#cwd = Path.cwd()
#34(cwd/'delicious'/'walnut'/'waffles').mkdir(parents=True)

#Absolute path -C:\Users\DELL\PythonBasics
print(Path.cwd()) #current working dir

print(Path('..').resolve())
#Path=Path.cwd()
#print(Path.is_absolute())

#Relative path
#You can get a relative path from a starting path to another path using pathlib
print(Path('/delicious/walnut').relative_to('/'))

#Path and File validity

print(Path('.').exists())
print(Path('demo.py').exists())

#Checking if it is a file
print(Path('filehandling.py').is_file())
#Checking if path is a dir
print(Path('delicious/walnut').is_dir())
stat=Path('filehandling.py').stat()
print(stat.st_size) # size in bytes

#for f in Path('/Users/DELL/PythonBasics').iterdir():
#    print(f)

#copying files or entire folders
#shutil.copy('test.txt', 'delicious/test2.txt') - copies single file
#shutil.copytree('/Users/DELL/PythonBasics', '/Users/DELL/Duplicate_Pythonbasics') --entire dir is copied to a new one and it is also performing mkdir
#shutil.copytree('/Users/DELL/PythonBasics','/Users/DELL/Duplicate_Pythonbasics',dirs_exist_ok=True)


#moving & renaming
#shutil.move('delicious/walnut/loop2.py', 'loops.py')

#deleting files & folders
#Calling Path.unlink() will delete the file at path.
#Calling Path.rmdir() will delete the folder at path. This folder must be empty of any files or folders.
#Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted
#The Path object has an rglob() method for recursively iterating over files and directories.
p = Path('/Users/DELL/PythonBasics')
for i in p.rglob('*'):
    print(i)

