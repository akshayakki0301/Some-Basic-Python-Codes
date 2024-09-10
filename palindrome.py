'''
def-the number which is equal to the reverse of itself is called palindrome number
'''
#reverse the number
n=int(input("enter the number:"))
rev=0
i=n
while i!=0:
    rem=n%10
    rev=rev*10+rem
    i=i//10
print("rev num=",rev)
if rev==n:
    print("palindrome")
else:
    print("is not palindrome")
    print(" ")