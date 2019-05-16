import os

try:
    file = open("myFile1905031117.txt", "w")
    file = open("myFile1905031118.txt", "w")
except IOError:
    file = open("myFile1905031117.txt", "a")
    file = open("myFile1905031118.txt", "a")



def barCalc():
    amount17 = 0
    amount18 = 0

    global newYn
    newYn = str(raw_input("New guest? y or n: "))


    if newYn =="0":
        guestName = str(raw_input("Input guest name:"))
        guestAge = float(input("Input guest age:"))
        guestAmount = float(input("Input the amount he want to spend:"))
        if guestAge > 18:
            f = open("myFile1905031118.txt", "a")
            amount18 = amount18 + guestAmount
            guestAmount=str(guestAmount)
            f.write(guestAmount)
            f.close()


        else:
            f = open("myFile1905031117.txt", "a")
            amount17 = amount17 + guestAmount
            guestAmount = str(guestAmount)
            f.write(guestAmount)
            f.close()

        barCalc()
    else:
        print amount17
        print amount18


barCalc()
