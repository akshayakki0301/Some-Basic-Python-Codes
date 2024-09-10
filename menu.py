print("1:Add\n2:Sub\n3:Mul\n4:Div")
n=int(input("enter you choice="))
if n==1:
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    Add=a+b
    print("the sum of entered number are:",Add)
elif n==2:
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    Sub=a-b
    print("the subtraction of entered number are:",Sub)
elif n==3:
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    Mul=a*b
    print("the Multiplication of entered number are:",Mul)
elif n==4:
    a=int(input("enter first number="))
    b=int(input("enter second number="))
    Div=a/b
    print("the division of entered number are:",Div)
else:
    print("wrong choice")
    
