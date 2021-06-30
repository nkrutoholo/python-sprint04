from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def print_stderr(msg):
    eprint(f'ERROR| {msg}.')
    sys.exit(1)

def oprint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)

def print_stdout(msg):
    oprint(f'INFO| {msg}.')
