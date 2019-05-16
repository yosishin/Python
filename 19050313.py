import os

firstFile = str(raw_input("Input first file name:"))
secondFile = str(raw_input("Input Second file name:"))

print (firstFile, secondFile)

def compare():
  f1 = open("firstFile", "r")
  f2 = open("secondFile", "r")
  for line1 in f1:
    for line2 in f2:
      if line1 == line2:
        print("SAME\n")
      else:
        print(line1 + line2)