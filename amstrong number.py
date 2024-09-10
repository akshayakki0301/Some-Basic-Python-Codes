#Armstrong Number
import math
n=int(input("enter the number:"))
c=0
i=n
while i!=0:
    c+=1
    i=i//10
print(" Count of the number is:",c)

sum=0
while i!=10:
    rem=i%10
    sum=sum+int(math.pow(rem,c))
    i+=1
if sum==n:
    print("the number is armstrong",n)
else:
    print("the number is not armstrong",n)
