from colorama import Fore
import os

def print_score(x, y, timespent, difficulty, color, type_play):
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
      
    if not os.path.exists("data"):
      os.mkdir("data")

    if not os.path.exists(f"data/leaderboard_{type_play}.csv"):
      with open(f"data/leaderboard_{type_play}.csv", "w") as f:
        f.write("")

    scores = []
    with open(f"data/leaderboard_{type_play}.csv", "r") as f:
      for line in f:
        scores.append(line.strip().split(","))
        
    if len(scores) < 5:
      scores.append([str(score), str(timespent), str(difficulty)])
      scores.sort(key=lambda x: x[0])
    else:
      scores.append([str(score), str(timespent), str(difficulty)])
      scores.sort(key=lambda x: x[0])
      scores.pop(0)
      
    if [str(score), str(timespent), str(difficulty)] in scores:
      print(Fore.GREEN + "\nYou made it to the leaderboard!")
    
    with open(f"data/leaderboard_{type_play}.csv", "w") as f:
      for score in scores:
        f.write(",".join(score) + "\n")
        
    print(Fore.CYAN + "\nTop 5 scores:")
    n = 1
    for score in scores:
      print(f"{n}. Score: {score[0]}, Time: {score[1]}, Difficulty: {score[2]}")
      n += 1

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
    
    # print leaderboard
    if not os.path.exists("data"):
      return
    else:
      scores = []
      with open(f"data/leaderboard_{type_play}.csv", "r") as f:
        for line in f:
          scores.append(line.strip().split(","))
          
      print(Fore.CYAN + "\nTop 5 scores:")
      n = 1
      for score in scores:
        print(f"{n}. Score: {score[0]}, Time: {score[1]}, Difficulty: {score[2]}")
        n += 1