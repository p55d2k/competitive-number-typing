from colorama import Fore
import random

def print_text(text, color, type):
  if color:
    colors = list(vars(Fore).values())
    colored_chars = [random.choice(colors) + char for char in str(text)]
    print(Fore.CYAN + f"\nYour {type} is: " + ''.join(colored_chars))
  else:
    print(Fore.CYAN + f"\nYour {type} is: " + str(text))