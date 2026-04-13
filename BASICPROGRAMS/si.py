p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate of interest:"))
n=int(input("Enter the year:"))
if(p>1 and p<100000 and r>1 and r<20 and n>1 and n<10):
   print("The simple interest is:",(p*n*r)//100)
else :
   print("Enter the priciple amount ,year,and interset rate according to the constraints:")
