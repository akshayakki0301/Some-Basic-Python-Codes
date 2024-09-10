sum=0
n=12345867655
i=n
while i!=0:
    rem=i%10
    sum=sum+rem
    i=i//10
print("Sum=",sum)  
