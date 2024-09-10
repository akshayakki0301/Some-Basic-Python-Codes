#reverse the number
n=int(input("enter the number:"))
rev=0
while n>0:
    i=n%10
    rev=rev*10+i
    n=n//10
print("rev num=",rev)
