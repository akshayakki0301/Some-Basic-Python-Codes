#1. Program to find maximum between two numbers:
print("#1. Program to find maximum between two numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Max is:", a)
else:
    print("Max is:", b)

print("\n")

#2. Program to find maximum between three numbers:
print("#2. Program to find maximum between three numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Max is:", a)
elif b >= a and b >= c:
    print("Max is:", b)
else:
    print("Max is:", c)

print("\n")

#3. Program to check whether a number is negative, positive or zero:
print("#3. Program to check whether a number is negative, positive or zero:")
n= int(input("Enter a number: "))

if n > 0:
    print("Number is positive")
elif n < 0:
    print("Number is negative")
else:
    print("Number is zero")

print("\n")

#4. Program to check whether a number is divisible by 5 and 11 or not:
print("#4. Program to check whether a number is divisible by 5 and 11 or not:")
n = int(input("Enter a number: "))

if n%5 == 0 and n%11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")

print("\n")

#5. Program to check whether a number is even or odd:
print("#5. Program to check whether a number is even or odd:")
n= int(input("Enter a number: "))

if n%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("\n")

#6.program to check whether a year is leap year or not.
print("#6.program to check whether a year is leap year or not.")
year=int(input("enter the year :"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("the year is leap year")
else:
    print("the year is not leap year")

print("\n")

#7.program to check whether a character is alphabet or not.
print("#7.program to check whether a character is alphabet or not.")
char = input("Enter a character: ")
if char.isalpha():
    print(char," is an alphabet.")
else:
    print(char," is not an alphabet.")

print("\n") 
#8.program to input any alphabet and check whether it is vowel or consonant.
print("#8.program to input any alphabet and check whether it is vowel or consonant.")
char = input("Enter an alphabet: ")
if char.lower() in 'aeiou':
    print(char," is a Vowel.")
else:
    print(char,"is a Consonant.")

print("\n")

#9.program to input any character and check whether it is alphabet, digit or special character.
print("#9.program to input any character and check whether it is alphabet, digit or special character.")
char = input("Enter an alphabet: ")
if char.isalpha():
    print(char," is an alphabet.")
elif char.isdigit():
    print(char," is a digit.")
else:
    print(char," is a Special character.")

print("\n")

#10.program to check whether a character is uppercase or lowercase alphabet.
print("#10.program to check whether a character is uppercase or lowercase alphabet.")
char = input("Enter an alphabet: ")
if char.upper():
    print(char," is an Upper.")
else:
    print(char," is an Lower.")

print("\n")

#11.program to input week number and print week day.
print("#11.program to input week number and print week day.")
wknum=int(input("enter the week number from 1-7:"))
if wknum==1:
    print("Monday")
elif wknum==2:
    print("Tuesday")
elif wknum==3:
    print("Wednesday")
elif wknum==4:
    print("Thursday")
elif wknum==5:
    print("Friday")
elif wknum==6:
    print("Saturday")
elif wknum==7:
    print("Sunday")
else:
    print("Invaild week number entered")

print("\n")

#12.program to input month number and print number of days in that month.
print("#12.program to input month number and print number of days in that month.")
motnum=int(input("enter the Month Number from 1-12:"))
if motnum in [1,3,5,7,8,10,12]:
    print("the month has 31 days")
elif motnum in [4,6,9,11]:
    print("the month has 30days")
elif motnum==2:
        year=int(input("enter the year :"))
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("the year is leap year")
        else:
            print("the year is not leap year")
else:
    print("Invaild month number entered")

print("\n")

#13.program to count total number of notes in given amount.
print("#13.program to count total number of notes in given amount.")
amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_counter = {}

for note in notes:
    if amount >= note:
        note_counter[note] = amount // note
        amount = amount % note

for note, count in note_counter.items():
    print(f"{note}: {count}")

#14.program to input angles of a triangle and check whether triangle is valid or not.
print("#14.program to input angles of a triangle and check whether triangle is valid or not.")
a=float(input("enter the first angle:"))
b=float(input("enter the second angle:"))
c=float(input("enter the third angle:"))
if (a+b+c)==180:
    print("triangle is vaild")
else:
    print("triangle is not vaild")
    
print("\n")

#15.program to input all sides of a triangle and check whether triangle is valid or not.
print("#15.program to input all sides of a triangle and check whether triangle is valid or not.")
a=float(input("enter the first side:"))
b=float(input("enter the second side:"))
c=float(input("enter the third side:"))
if a+b>c and b+c>a and a+c>b:
    print("triangle is vaild")
else:
    print("triangle is not vaild")

print("\n")
    
#16.program to check whether the triangle is equilateral, isosceles or scalene triangle.
print("#16.program to check whether the triangle is equilateral, isosceles or scalene triangle.")
a=float(input("enter the first side:"))
b=float(input("enter the second side:"))
c=float(input("enter the third side:"))
if a==b==c:
    print("triangle is equilateral")
elif a==b or a==c or b==c:
    print("triangle is isosceles")
else:
    print("triangle is scalene")

print("\n")
   
#17.program to find all roots of a quadratic equation.
print("#17.program to find all roots of a quadratic equation.")
import cmath
a=int(input("coffectient of a:"))
b=int(input("coffectient of b:"))
c=int(input("coffectient of c:"))
root1=(-b+cmath.sqrt(b**2-4*a*c))/2*a
root2=(-b-cmath.sqrt(b**2-4*a*c))/2*a
print("the first root is:",root1)
print("the second root is:",root2)

print("\n")

#18.program to calculate profit or loss.
print("#18.program to calculate profit or loss.")
cstprice=float(input("enter the cost price:"))
selprice=float(input("enter the selling price:"))
if cstprice>selprice:
    print("You get Loss for  ",cstprice-selprice,"amount")
elif selprice>cstprice:
    print("You get profit for  ",selprice-cstprice,"amount")
else:
    print("no profit ,no loss")

print("\n")

#19.program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
print("#19.program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.\nCalculate percentage and grade according to following:")
'''
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''

Physics=float(input("Enter the marks for Physics:"))
Chemistry=float(input("Enter the marks for Chemistry:"))
Biology=float(input("Enter the marks for Biology:"))
Mathematics=float(input("Enter the marks for Mathematics:"))
Computer=float(input("Enter the marks for Computer:"))
t= Physics+Chemistry+Biology+Mathematics+Computer
p=(t/500)*100
if p>=90:
    print("Grade A  ",p,"%")
elif p>=80:
    print("Grade B  ",p,"%")
elif p>=70:
    print("Grade C  ",p,"%")
elif p>=60:
    print("Grade D  ",p,"%")
elif p>=40:
    print("Grade E  ",p,"%")
elif p<40:
    print("Grade F  ",p,"%")
else:
    print("Fail ",p,"%")

print("\n")

#20.program to input basic salary of an employee and calculate its Gross salary according to following:
print("#20.program to input basic salary of an employee and calculate its Gross salary according to following:")
'''
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%
'''
bs=int(input("enter the Basic Salary:"))
if  bs<=10000 :
    hra=bs*0.2
    da=bs*0.8
    gs=bs+hra+da
    print("Gross Salary of employee is:",gs)
elif bs<=20000:
    hra=bs*0.25
    da=bs*0.9
    gs=bs+hra+da
    print("Gross Salary of employee is:",gs)
elif bs>20000:
    hra=bs*0.3
    da=bs*0.95
    gs=bs+hra+da
    print("Gross Salary of employee is:",gs)
else:
    print("enter the vaild Salary")
    
print("\n")

#21.program to input electricity unit charges and calculate total electricity bill according to the given condition:
print("#21.program to input electricity unit charges and calculate total electricity bill according to the given condition:")
'''
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 150 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill
x       
'''
units=int(input("enter the electricity unit charge:"))
if units<=50:
    bill=units*0.50
elif units<=100:
     bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units<=150:
   bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill=(50*0.50)+(100*0.75)+(150*1.20)+((units-250)*1.50)
subcharge=bill*0.20
total=bill+subcharge
print("the  total electricity bill is",total)
