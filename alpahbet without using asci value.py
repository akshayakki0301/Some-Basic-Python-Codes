'''
A 
A B 
A B C 
A B C D 
A B C D E
'''
k=64
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+k),end=" ")
    print()
