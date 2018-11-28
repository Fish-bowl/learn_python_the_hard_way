#6

# types_of_people = 10 
# x = f"There are {types_of_people} types of people."

# binary = "binary"
# do_not = "don't"
# y = f"Thoes who know {binary} and thoes who {do_not}"

# print(x)
# print(y)
# print(f"I said: {x}")
# print(f"I also said: '{y}'")

# hilarious = False 
# joke_evaluation = "Isn't that joke so funny? {}"

# print(joke_evaluation.format(hilarious))

# w = "This is the left side of..."
# e = "a string with a right side."
# print(w + e)

#7

# print("Mary had a little lamb.")
# print("It's fleece was white as {}.".format('snow'))
# print("And everywhere that Mary went.")
# print("." * 10)

# end1 = 'C'
# end2 = 'H'
# end3 = 'E'
# end4 = 'E'
# end5 = 'S'
# end6 = 'E'
# end7 = 'B'
# end8 = 'U'
# end9 = 'R'
# end10 = 'G'
# end11 = 'E'
# end12 = 'R'

# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print(end7 + end8 + end9 + end10 + end11 + end12)
 
#8

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "this is a haiku",
  "I think it's pretty darn good",
  "but then again, maybe not"
))
