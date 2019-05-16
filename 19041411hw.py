n=float(input("Enter number:"))
point=1
idNumber=[]
itemB=1
totalSum=0

while point >0:
    n = float(n)
    n=float(n/10)
    print n
    newNumber=int((n-(int(n)))*10)
    idNumber.insert(0,newNumber)
    print idNumber
    n=int(n)
    n=float(n)
    if (n > 0):
        point=1
    else:
        point=0
else:
    while len(idNumber) <9:
        idNumber.insert(0, 0)
        print idNumber

for x in range(0,9):
    idNumber[x]=idNumber[x]*itemB
    if ( x % 2== 0):
        itemB=2
    else:
        itemB=1
    print idNumber

for x in range(0,10):
    if (idNumber[x]>9):
        idNumber[x]=float(idNumber[x])
        fDigit=int(idNumber[x]/10)
        print "fDigit " , fDigit
        sDigit=(idNumber[x]-fDigit)*10
        print "sDigit " , sDigit
        sumDigit=fDigit+sDigit
        print sumDigit
        totalSum=totalSum+sumDigit
        print totalSum

    else:
        totalSum = totalSum + idNumber[x]
        print totalSum





