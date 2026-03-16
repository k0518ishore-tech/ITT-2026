#  a snd b has competion of who has maximum no of coins (it has three rounds).add  c with losser of round 1. then add d with loser of round 2. final round select  the winner 

a,b,c,d=(int(i) for i in input("").split())
if b > a:
   a = a+c
else:
   b = b+c
if b > a:
   a = a+d
else:
   b = b+d
if b > a:
   print("S")
else:
   print("N")
