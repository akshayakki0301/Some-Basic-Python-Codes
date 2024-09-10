'''#19. Program to find frequency of each digit in a given number:
print("#19. Program to find frequency of each digit in a given number:")

num = int(input("Enter a number: "))
frequency = [0] * 10

while num > 0:
    digit = num % 10
    frequency[digit] += 1
    num //= 10

for i in range(10):
    if frequency[i] != 0:
        print(f"Digit {i} occurs {frequency[i]} times")
#20. Program to print pyramid/triangular pattern using nested for loops:
print("#20. Program to print pyramid/triangular pattern using nested for loops:")
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
'''
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
