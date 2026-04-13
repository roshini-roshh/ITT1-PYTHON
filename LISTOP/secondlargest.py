l=[]

for i in range(3):
    n=int(input("Enter the three elements:"))
    l.append(n)
l.sort(reverse=True)
print("Second largest:",l[1])
for i in range(3):
   print(l[i])
