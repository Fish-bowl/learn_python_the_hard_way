  # close = closes file
  # read = reads file
  # readline = reads oneline
  # trunicate = empty file !caution
  # write("stuff") = writes "stuff" to file
  # seek(0) = move the reac/write location to beginning of file 

from sys import argv 
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that hit ctrl-c.")
print("if you do, hit return")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now im going ot ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1, "\n", line2, "\n", line3, "\n" )
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("and finally, we close it")
target.close()
