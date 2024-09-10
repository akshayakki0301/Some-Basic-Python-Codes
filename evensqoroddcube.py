#even or odd number
a=int(input("enter the number :"))
rem=a%2
if rem == 0:
    print("the number",a,"is even number\nthe square of number is ", a**2)
else:
    print("the number ",a,"is odd number\nthe cube of the number is ", a**3)
