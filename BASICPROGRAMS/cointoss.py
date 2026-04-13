a=int(input("ENter no of coins A holds:"))
b=int(input("ENter no of coins B holds:"))
c=int(input("Enter the no of coins C holds:"))
d=int(input("Enter no of coins D holds:"))
awin=a
bwin=b
if a<b or a==b:
        awin+=c
        if a>b:
                print("S")
     ## print("SURESH WINS THE GAME")
        elif b<awin:
                bwin+=d
                if awin>bwin or awin==bwin:
                        print("S")
                else:
                        print("N")
else:
   print("S")
