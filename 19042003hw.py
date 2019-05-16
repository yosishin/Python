#x = input('Enter string:')
#y = len(x)
#z = input ('input key')

x="qwertyuiop"
y = len(x)
z="r"

print x





def myFunc():


    if z==x[y]:
        print "item "+ z + " is in the string"
        y=y-1
        if y>0:
            myFunc
    else:
        print "item", z, "is not the string"


myFunc()

