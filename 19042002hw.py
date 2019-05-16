x = input('Enter first number:')
y = input('Enter Second number:')
sum=x
y=y-1

def myFunc():
    global y
    global x
    global sum
    if y!=0:
        if y>0:
            sum=sum+x
            y = y-1
            myFunc()
        else:
            print sum

    else:
        print sum





myFunc()
