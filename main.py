import os
os.system("pip install colorama")
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from getpass import getpass
from colorama import Fore
import random
import json
import time

if not os.path.exists("settings.json"):
  with open("settings.json", "w") as f:
    json.dump({"color": False}, f)
with open("settings.json", "r") as f:
  settings = json.load(f)

print(Fore.WHITE + "\033cCOMPETITIVE NUMBER TYPING")
print("Type 'exit' to exit the game.")

n = -1
while n <= 10:
  n = input(Fore.GREEN + "\nChoose the level of difficulty (>10): " + Fore.WHITE).strip().lower()

  if n == "exit":
    exit()

  if not n.isdigit():
    print(Fore.RED + "Invalid format. Try again.")
    n = -1
    continue

  n = int(n)
  if n <= 10:
    print(Fore.RED + "Enter a number greater than 10.")
    n = -1
    continue

x = random.randint(10 ** (n-1), (10 ** n) - 1)

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
  score = round((timespent / n) * 100, 3)
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
  print(Fore.RED + f"Wrong! You typed {y}. \nYour rank is Skill Issue. You have a skill issue.")