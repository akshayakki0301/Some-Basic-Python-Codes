i=1
while i<=100:
    j=i
    rev=0
    while j!=0:
        rem=j%10
        rev=rev*10+rem
        j=j//10
    if rev==i:
        print(i,end=" ")
    i+=1
