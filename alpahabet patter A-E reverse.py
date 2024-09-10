'''
E D C B A 
E D C B 
E D C 
E D 
E 

'''
for i in range(65,70):
    for j in range(69,i-1,-1):
        print(chr(j),end=" ")
    print()
