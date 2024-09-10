sum=0
n=23456789
i=n
while i!=0:
    rem=i%10
    if rem%2==1:
        sum=sum+rem
    i=i//10
print("Sum=",sum)  

