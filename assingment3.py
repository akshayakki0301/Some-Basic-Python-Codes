#1. Program to print numbers from 1 to 10 using a for loop:
print("#1. Program to print numbers from 1 to 10 using a for loop:")
for i in range(1, 11):
    print(i,end=" ")

print("\n")

#2. Program to calculate the sum of first 10 natural numbers using while loop:
print("#2. Program to calculate the sum of first 10 natural numbers using while loop:")   
sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
print("the sum of first Natural number",sum,end=" ")

print("\n")

#3. Program to print numbers from 1 to 15 using a do-while loop (simulated with a while loop in Python):
print("#3. Program to print numbers from 1 to 15 using a do-while loop (simulated with a while loop in Python):")   
i=1
while True:
    print(i,end=" ")
    i=i+1
    if i>15:
        break

print("\n")

#4. Program to print the even numbers between 10 and 30 using for loop:
print("#4. Program to print the even numbers between 10 and 30 using for loop:")
for i in range(10,31):
    if i%2==0:
        print(i,end=" ")


#5. Program to find factorial of a given number using while loop:
print("#5. Program to find factorial of a given number using while loop:")
i=1
n=int(input("enter the number:"))
fact=0
while i<=n:
    fact*=i
    i+=1
print("the factorial of the number is :",fact)

print("\n")

#6. Program to print the multiplication table of a given number using for loop:
print("6. Program to print the multiplication table of a given number using for loop:")
n= int(input("Enter a number: "))
for i in range(1, 11):
    
    print(n,"x",i,"=",n*i)

print("\n")
#7. Program to check if a given number is prime or not using while loop:
print("#7. Program to check if a given number is prime or not using while loop:")
n=int(input("enter the number:"))
i=2
while i<=n:
    if n%i==0:
        break
    i+=1
if n==i:
    print("Prime Number")
else:
    print("Not a Prime number")

print("\n")

#8. Program to calculate the sum of digits of a given number using do-while loop (simulated with a while loop in Python):
print("#8. Program to calculate the sum of digits of a given number using do-while loop (simulated with a while loop in Python):")
n=int(input("enter the number:"))
sum=0
while True:
    sum=sum+n%10
    n=n//10
    if n==0:
        break
print("the sum of inputed number is=",sum)

print("\n")

#9. Program to count number of digits in a given number using for loop:
print("#9. Program to count number of digits in a given number using for loop:")
n= int(input("Enter a number: "))
count = 0
for i in str(n):
    count += 1
print("Number of digits:", count)

print("\n")

#10. Program to reverse a given number using for/while loop:
print("10. Program to reverse a given number using for/while loop:")
n=int(input("Enter a number: "))
rev=0
while n>0:
   rev=rev*10+n%10
   n=n//10
print(rev,end=" ")
   
print("\n")

#11. Program to check if a given number is palindrome or not using while loop:
print("#11. Program to check if a given number is palindrome or not using while loop:")
n= int(input("Enter a number: "))
i= n
rev= 0
while n> 0:
    rev= rev* 10 + n% 10
    n//= 10
if i==n:
    print(i," is a palindrome")
else:
    print(i,"is not a palindrome")
   
print("\n")

#12. Program to print Fibonacci series up to 10 terms using for loop:
print("#12. Program to print Fibonacci series up to 10 terms using for loop:")
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b
   
print("\n")

#13. Program to find GCD of two given numbers using while loop:
print("#13. Program to find GCD of two given numbers using while loop:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b

print("GCD is:", a)
   
print("\n")

#14. Program to print all factors of a given number using do-while loop (simulated with a while loop in Python):
print("14. Program to print all factors of a given number using do-while loop (simulated with a while loop in Python):")
num = int(input("Enter a number: "))
i = 1
while True:
    if num % i == 0:
        print(i)
    i += 1
    if i > num:
        break
   
print("\n")

#15. Program to calculate simple interest using loop to take number of years as input:
print("#15. Program to calculate simple interest using loop to take number of years as input:")
p= float(input("Enter principal amount: "))
r= float(input("Enter rate of interest: "))
year= int(input("Enter number of years: "))

for year in range(1, year+ 1):
    simple_interest = (principal * rate * year) / 100
    print("Year ",year," Simple Interest = ",simple_interest")

   
print("\n")
          
#16. Program to find largest among 10 given numbers using nested for loops:
print("#16. Program to find largest among 10 given numbers using nested for loops:")
num= 
print("\n")

#17. Program to make a simple calculator using switch case and do-while loop (simulated with a while loop in Python):
print("#17. Program to make a simple calculator using switch case and do-while loop (simulated with a while loop in Python):")
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        break
    num1= float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice==1:
        Add=num1+num2
        print("the sum of entered number are:",Add)
        print()
    elif choice==2:
        Sub=num1-num2
        print("the subtraction of entered number are:",Sub)
        print()
    elif choice==3:
        Mul=num1*num2
        print("the Multiplication of entered number are:",Mul)
        print()
    elif choice==4:
        Div=num1/num2
        print("the division of entered number are:",Div)
        print()
    else:
        print("wrong choice")
        print()
    
   
print("\n")


#18. Program to print prime numbers between given range using for loop:
print("#18. Program to print prime numbers between given range using for loop:")

strt = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for i in range(strt, end + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)
   
print("\n")

#19. Program to find frequency of each digit in a given number:
print("#19. Program to find frequency of each digit in a given number:")

print("\n")
#20. Program to print pyramid/triangular pattern using nested for loops:
print("#20. Program to print pyramid/triangular pattern using nested for loops:")

print("\n")
