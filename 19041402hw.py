n=float(input("Enter number:"))
t1=n
print t1
t2=0
rev=0
while(int(t1/10))>0:
    t1=float(t1/10)
    print t1
    t2=t1-int(t1)
    print t2
    rev = rev * 10 + t2 * 10
    print rev
    t1 = int(t1)
    print t1
if(n==rev):
    print("This is palindrome")
else:
    print("This is not palindrome")




