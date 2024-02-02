import os
type_play = input("\033cCompetitive word typing or competitive number typing? (w/n): ").strip().lower()
if type_play == "w":
  os.system("python3 src/word.py")
elif type_play == "n":
  os.system("python3 src/number.py")
  