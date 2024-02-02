from start import *
from difficulty import get_difficulty
from colors import print_text
from score import print_score
import string

print(Fore.WHITE + "\033cCOMPETITIVE WORD TYPING")
print("Type 'exit' to exit the game.")

difficulty = get_difficulty()
x = ''.join(random.choices(string.ascii_lowercase, k=difficulty))

print_text(x, settings["color"], "word")

starttime = time.time()
run = True

while run:
  guess = getpass(Fore.WHITE + "Guess the word: ").strip().lower()
  
  if guess == "exit":
    exit()
    
  if not guess.isalpha():
    print(Fore.RED + "Invalid format. Try again.")
    starttime = time.time()
    
  else:
    y = guess
    endtime = time.time()
    run = False

timespent = round(endtime - starttime, 3)

print_score(x, y, timespent, difficulty, settings["color"], "word")
time.sleep(10)
