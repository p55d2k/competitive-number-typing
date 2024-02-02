from colorama import Fore

def get_difficulty():
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
  return difficulty