#prime number
n=int(input("enter the number:"))
i=2
while i<=n:
    if n%i==0:
        break
    i+=1
if n==i:
    print("Prime Number")
else:
    print("Not a Prime number")
