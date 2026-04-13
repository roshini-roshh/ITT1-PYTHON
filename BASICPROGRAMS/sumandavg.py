m1=int(input("Enter the mark 1:"))
m2=int(input("Enter the mark 2:"))
m3=int(input("Enter the mark 3:"))
if(0<=m1 and m2 and m3<=100):
   print("Sum is:",m1+m2+m3)
   print("Average is:",(m1+m2+m3)//3)
else:
   print("Enter the marks according to the constraints")
