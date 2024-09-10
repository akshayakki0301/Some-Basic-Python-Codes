#A grocery shop launch discount system, if the bill value>1000 then 10% discount will be given
bill=float(input("enter the bill amount="))
dis=0
if bill>1000:
    dis=bill*0.1
    print(" your bill amt is=",bill)
    print("discount amount=",dis)
    print("total amount to pay=",bill-dis)
else:
    print(" your bill amt is=",bill)
    print("discount amount=",dis)
    print("total amount to pay=",bill-dis)
