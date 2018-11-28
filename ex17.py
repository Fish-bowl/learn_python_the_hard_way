from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#oneline?
in_file = open(from_file)
indata = in_file.read()
# indata = from_file.read()


print(f"The input file is {len(indata)} bytes long")
out_file = open(to_file, 'w')
out_file.write(indata)
print("." * 10)
print("Alright, all done")

out_file.close()
in_file.close()
