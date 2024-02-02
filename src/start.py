import os
os.system("pip install colorama")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from getpass import getpass
from colorama import Fore
import random
import json
import time
import sys

# allow for large numbers
sys.set_int_max_str_digits(2147483647)

if not os.path.exists("../settings.json"):
  with open("../settings.json", "w") as f:
    json.dump({"color": False}, f)
with open("../settings.json", "r") as f:
  settings = json.load(f)
