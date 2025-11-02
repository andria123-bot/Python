# dice rolling simulator

import random

x = "y"

while x == "y":
  no = random.randint(1, 6)
  
  if no == 1:
    print("[-----]")
    print("|     |")
    print("|  O  |")
    print("|     |")
    print("[-----]")
  
  if no == 2:
    print("[-----]")
    print("| O   |")
    print("|     |")
    print("|   O |")
    print("[-----]")
  
  if no == 3:
    print("[-----]")
    print("|     |")
    print("|O O O|")
    print("|     |")
    print("[-----]")
  
  if no == 4:
    print("[-----]")
    print("|O   O|")
    print("|     |")
    print("|O   O|")
    print("[-----]")
    
  if no == 5:
    print("[-----]")
    print("|O   O|")
    print("|  O  |")
    print("|O   O|")
    print("[-----]")
    
  if no == 6:
    print("[-----]")
    print("|O   O|")
    print("|O   O|")
    print("|O   O|")
    print("[-----]")
  x = input("Prees y yo roll again and n to exit: ")
  print("\n")