
i = int(input("> "))
print("what would you like to add by")
add_by = int(input("> "))

def adder(i):
  numbers = []

  while i <= 10:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + add_by
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


  print("Numbers now: ")

  for num in numbers:
    print(num)

adder(i)
