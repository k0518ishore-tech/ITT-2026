#This program  will return yes it the tyre can form bike and car if no then it can form only bike or car or none of these
n = int(input("ENTER THE NO OF TYER:"))
if n!= 0:
   num = n%4
   if num == 0 :
      print("NO")
   elif num%2 == 0:
      print("yes")
   else:
      print ("no")
