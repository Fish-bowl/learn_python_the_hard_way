from sys import exit 


def create_char():
  print("what is your name?")
  name = input("> ")
  print("What is your gender?")
  print("M or F?")
  gender = input("> ")
  print("and your age is?")
  age = input("> ")
  print(f"so your name is {name}, your're a {gender}, and your {age} yesrs old.")
  print("what style fighter are you"?)
  print("Mage, Knight, Monk, or Ranger")
  style = input("> ")
  char = [name, gender, age, style,]

def gold_room():
  print("This room is full of gold. How much do you take?")

  choice = int(input("> "))
  if choice == 1 or choice == 0:
    dead("Man, learn to type a number.")
  elif choice < 50:
    print(f"you wanted {choice} gold coins.")
    print("Nice, you're not greedy, you win!")
    exit(0)
  else: 
    print(f"you wanted {choice}...")
    dead("You greedy bastard!")


def bear_room():
  print("There is a bear in here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False

  while True:
    choice = input("> ")

    if choice == "take honey":
      dead("The bear looks at you, then slaps your face off")
    elif choice == "taunt bear" and not bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your leg off")
    elif choice == "open door" and bear_moved:
      gold_room()
    else: 
      print("I got no idea what that means.")

def cthulu_room():
  print("Here you see the great evil Cthulu.")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life or eat your head?")

  choice = input("> ")

  if 'flee' in choice:
    game()
  elif 'head' in choice:
    dead("well that was tasty")
  else: 
    cthulu_room()

def dead(why):
  print(why, "good job!")
  exit(0)

def game():
  print("You are in a dark room.")
  print("There is a door to your right and left.")
  print("Which do you take?")
  choice = input("> ")

  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulu_room()
  else:
    dead("You stuble around the room until you starve")

def intro():
  print("welcome to my game!")
  print("1. to play")
  print('2. to exit')
  choice = int(input("> "))
  if choice == 1:
    game()
  elif choice == 2:
    exit(0)


intro()
