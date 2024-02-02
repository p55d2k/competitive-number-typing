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

if not os.path.exists("settings.json"):
  with open("settings.json", "w") as f:
    json.dump({"color": False}, f)
with open("settings.json", "r") as f:
  settings = json.load(f)

print(Fore.WHITE + "\033cCOMPETITIVE NUMBER TYPING")
print("Type 'exit' to exit the game.")

difficulty = -1
while difficulty <= 10:
  difficulty = input(Fore.GREEN + "\nChoose the level of difficulty (>10): " + Fore.WHITE).strip().lower()

  if difficulty == "exit":
    exit()

  if not difficulty.isdigit():
    print(Fore.RED + "Invalid format. Try again.")
    difficulty = -1
    continue

  difficulty = int(difficulty)
  if difficulty <= 10:
    print(Fore.RED + "Enter a number greater than 10.")
    difficulty = -1
    continue

x = random.randint(10 ** (difficulty - 1), (10 ** difficulty) - 1)

if settings["color"]:
  colors = list(vars(Fore).values())
  colored_chars = [random.choice(colors) + char for char in str(x)]
  print(Fore.CYAN + "\nYour number is: " + ''.join(colored_chars))
else:
  print(Fore.CYAN + "\nYour number is: " + str(x))

starttime = time.time()
run = True

while run:
  guess = getpass(Fore.WHITE + "Guess the number: ").strip().lower()
  
  if guess == "exit":
    exit()
    
  if not guess.isdigit():
    print(Fore.RED + "Invalid format. Try again.")
    starttime = time.time()
    
  else:
    y = int(guess)
    endtime = time.time()
    run = False

timespent = round(endtime - starttime, 3)

if x == y:
  score = round((timespent / difficulty) * 100, 3)
  if settings["color"]:
    score -= 2

  print(Fore.GREEN + f"\nCorrect! Your time is {timespent}. \nYour score is {score}.")
  if score > 100:
    print(Fore.GREEN + "Your rank is Sloth. Get better.")
  elif score > 75:
    print(Fore.GREEN + "Your rank is Tortoise. Try again.")
  elif score > 50:
    print(Fore.GREEN + "Your rank is Panda. Not bad.")
  elif score > 25:
    print(Fore.GREEN + "Your rank is Kangaroo. Good job!")
  elif score > 0:
    print(Fore.GREEN + "Your rank is Cheetah. Excellent!")
  else:
    print(Fore.GREEN + "Your rank is Cheater. You are a cheater.")
else:
  print(Fore.RED + f"\nWrong! You typed {y}. \nYour rank is Skill Issue. You have a skill issue.\nYour time was {timespent}.")