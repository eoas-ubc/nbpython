import sys
from pathlib import Path

path = Path(__file__).resolve()  # this file
this_dir = path.parent  # this folder
lib_dir = this_dir.parent
sys.path.insert(0, str(lib_dir.resolve()))
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n{sys.path[-1]}\n{sep}\n")

print(f"through {__file__}")
