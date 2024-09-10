#take a number check it is completely divisible by 3 and 9
num=int(input ("enter the number="))
if (num%3==0):
    if (num%9==0):
        print("the number is divisible 3 and 9")
else:
    print("the number is  not divisible 3 and 9")
