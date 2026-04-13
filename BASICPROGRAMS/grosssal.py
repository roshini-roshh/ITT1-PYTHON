h=int(input("Enter the house rent allowance:"))
d=int(input("Enter the da:"))
b=int(input("Enter basic salary:"))
hra=h*(20/100)
da=d*(10/100)
g=b+hra+da
if(5000 <= b <=50000):
   print("Gross salary :",g)
else:
   print("ENTER VALUES ACCORDING TO THE CONSTRAINTS")
