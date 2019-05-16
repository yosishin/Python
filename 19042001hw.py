myArry =["lidor", "Lahav", "Grim", "Alona", "Eyal", "Avichai"]
n=len(myArry)

def funcPrint():
    global n
    n=n-1
    print myArry[n]
    if n>0:
        funcPrint()



funcPrint()

