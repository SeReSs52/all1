from cx_Freeze import setup, Executable
from cx_Freeze import setup, Executable
import sys
base=None
if sys.platform == "win31" : base = "Win32GUI"
opts = {'include_files': ['music.mp3'], 'includes': ['tkinter', 'pygame', 'pyautogui']}
setup(
    name = 'word',
    version = 0.1,
    description = "Simple Word",
    options = {'build_exe': opts},
    executables = [Executable('virusepelepsia.py', base= base)])