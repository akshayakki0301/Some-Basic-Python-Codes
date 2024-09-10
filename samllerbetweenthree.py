#take three number and print the smallers between them
a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
if a<b:
    if a<c:
        print("first number is smaller",a)
if b<a:
    if b<c:
         print("second number is smaller",b)
if c<a:
    if c<b:
        print("third the number is smaller",c) 
