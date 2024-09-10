#wapp  to accept three number if the number is greater than 100 then print sum of the two number if second number is greater than 100 then print subtraction of two number ,else print the pr
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>100:
    print("addtion of first two number is ",b+c);
elif b>100:
    print("subtraction of two number is",a-c);
else:
    print("product of all number is ",a*b*c);
