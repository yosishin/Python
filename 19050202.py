import os.path, time

try:
    file = open("c:\\users\\hackeru\\desktop\\newDir\\020519File.txt", "a+")
except:
    pass



timeUpdate= "Last modified: %s" % time.ctime(os.path.getmtime("c:\\users\\hackeru\\desktop\\newDir\\020519File.txt"))
print timeUpdate

file.write(timeUpdate)
file.write("\n")