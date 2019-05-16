arryCars = ["Ford", "Volvo", "BMW", "VW", "Fiat"]
n=len(arryCars)

def class1():
    global n
    n=n-1
    print arryCars[n]
    if n>0:
        class1()



class1()
