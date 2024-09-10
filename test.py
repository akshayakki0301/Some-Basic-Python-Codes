'''
take a 5 digit number and print the sum of  sqaure even digit
'''
n=12645
i=n
sum=0
while i!=0:
    rem=i%10
    if rem%2==0:
        sum=sum+rem
        print("Sum of the even number is:",sum)
    i=i//10
