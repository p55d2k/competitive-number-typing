from start import *
from difficulty import get_difficulty
from colors import print_text
from score import print_score

print(Fore.WHITE + "\033cCOMPETITIVE NUMBER TYPING")
print("Type 'exit' to exit the game.")

difficulty = get_difficulty()
x = random.randint(10 ** (difficulty - 1), (10 ** difficulty) - 1)

print_text(x, settings["color"], "number")

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

print_score(x, y, timespent, difficulty, settings["color"], "number")
time.sleep(10)
