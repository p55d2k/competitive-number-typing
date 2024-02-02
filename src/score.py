from colorama import Fore

def print_score(x, y, timespent, difficulty, color):
  if x == y:
    score = round((timespent / difficulty) * 100, 3)
    if color:
      score -= 2

    print(Fore.GREEN + f"\nCorrect! Your time is {timespent}. \nYour score is {score}.")
    # a different score for each rank
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
      print(Fore.RED + "Your rank is Cheater. You are a cheater.")
  else:
    print(Fore.RED + f"\nWrong! You typed {y}.")

    print(Fore.CYAN + f"The difference is highlighted in red: ", end="")
    for i in range(len(str(x))):
      if i < len(str(y)):
        if str(x)[i] == str(y)[i]:
          print(Fore.GREEN + str(x)[i], end="")
        else:
          print(Fore.RED + str(x)[i], end="")
      else:
        print(Fore.RED + str(x)[i], end="")

    print(Fore.RED + f"\n\nYour rank is Skill Issue. You have a skill issue.")
    print(Fore.RED + f"Your time was {timespent}.")