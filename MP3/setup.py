import os.path
import sys

from cx_Freeze import setup,Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

#A
build_exe_options = {"packages": ["os"], 'include_files':['tcl86t.dll', 'tk86t.dll',]}

#A
#A
base = None
if sys.platform == "win32":
    base = "win32GUI"

#options = {
 #   'build_exe': {
 #       'include_files': [
 #           os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
 #           os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t'),
 #      ],
 #   },
#}

setup(name="MP3",
      version="0.1",
      description="MP3 MUSIC PLAYER build using python Tkinter by @AaShUtOsH PaNcHoLi",
      options={"build_exe": build_exe_options},
      executables=[Executable("main.py", base=base)])
