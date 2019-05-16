newFile1 = str(raw_input("Enter first file name and adress: "))
newFile2 = str(raw_input("Enter second file name and adress: "))

text_file1 = open(newFile1, "r")
lines1 = str(text_file1.readlines())
print lines1
print len(lines1)

text_file2 = open(newFile2, "r")
lines2 = str(text_file2.readlines())
print lines2
print len(lines2)

index = 0
def compFile():
    global index
    if lines1[index]==lines2[index]:
        index=index+1
        if index< len(lines1):
            compFile()
        else:
            print "1"
    else:
        print "0"

compFile()






