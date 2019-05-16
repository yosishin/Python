newFileAd = str(raw_input("Enter file name and adress: "))

text_file = open(newFileAd, "r")
lines = str(text_file.readlines())
print lines
print len(lines)

try:
    file = open("myFile19050713.txt", "w")
except IOError:
    file = open("myFile19050713.txt", "a")

data = lines.split(",")
for temp in data:
    if len(temp)>5:
        print temp
        f = open("myFile19050713.txt", "a")
        f.write(temp)
        f.close()

text_file.close()
