import webbrowser
import re
import sys
from helper import print_stderr, print_stdout

if len(sys.argv) == 1:
    print_stderr("The site URL was not passed.")
elif not re.match("^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$", sys.argv[1]):
    print_stderr('The site URL format is invalid')
else:
    print_stdout(f"Opening the YouTube video at {sys.argv[1]}")
    webbrowser.open(sys.argv[1])
    print_stdout("YouTube video opened")
