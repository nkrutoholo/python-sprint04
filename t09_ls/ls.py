import os, sys

if len(sys.argv) < 2:
    os.system(f"ls")
elif len(sys.argv) == 2:
    os.system(f"ls {sys.argv[1]} | grep -v '^total' | sed -E '2,$s/ +[0-9]+//'")
elif len(sys.argv) == 3:
    if '-' in sys.argv[1]:
        os.system(f"ls {sys.argv[1]} {sys.argv[2]} | grep -v '^total' | sed -E '2,$s/ +[0-9]+//'")
    else:
        os.system(f"ls {sys.argv[2]} {sys.argv[1]} | grep -v '^total' | sed -E '2,$s/ +[0-9]+//'")
