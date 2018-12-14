def addition():
  print("Give me a number")
  num = int(input("> "))
  print("what would you like to add by")
  mod = int(input("> "))
  final_num = num + mod
  print("{} + {} = {}".format(num, mod, final_num))
  start()

def subtraction():
  print("Give me a number")
  num = int(input("> "))
  print("what would you like to subtract by")
  mod = int(input("> "))
  final_num = num - mod
  print("{} - {} = {}".format(num, mod, final_num))
  start()

def multiplication():
  print("Give me a number")
  num = int(input("> "))
  print("what would you like to multipy by")
  mod = int(input("> "))
  final_num = num * mod
  print("{} * {} = {}".format(num, mod, final_num))
  start()

def division():
  print("Give me a number")
  num = int(input("> "))
  print(f"what would like to divide {num} by?")
  mod = int(input("> "))
  final_num = num / mod
  print("{} / {} = {}".format(num, mod, final_num))
  start()

def start():
  print("what kind of math would you like to do?")
  print("""
  * ) multiplication,
  - ) subtraction,
  + ) addition, 
  / ) division.
  """)
  choice = input(">")
  if choice == "*" or choice == 'multiply' or choice == "multiplication":
    multiplication()
  elif choice == "-" or choice == "subtract" or choice == "subtraction":
    subtraction()
  elif choice == "+" or choice == "add" or choice == "addition":
    addition()
  elif choice == '/' or choice == 'divide' or choice == "division":
    division()
  else:
    start()
start()
