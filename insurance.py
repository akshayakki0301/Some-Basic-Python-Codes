'''A company has introduce insurance plan for his employee  Driver , The dirver is married
insurance will be given. if the driver is male, unmarried , > 32 then insurance will be provided.
If the driver is female, unmarrried  age  >26 the insurance will be provided.'''

dirver_status=input("enter the status Married or Unmarried:")
if  dirver_status== "married":
    print("Insurance will be given")

else:
    dirver=input("enter the gender of the Dirver:")
    dirver_Age=int(input("enter the age of Dirver:"))

    if dirver=="male":
        if  dirver_Age>32:
            print("The Insurance will given ")
        else:
            print("The Insurance will not given ")

    if dirver=="female":
        if  dirver_Age>26:
            print("The Insurance will given ")
        else:
            print("The Insurance will not given ")
