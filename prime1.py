no=int(input("enter a number:"))
count=0
i=2
while i<=no/2:
       if no%i==0:
              count=1
              break
       i=i+1
if count==0:
       print("number is prime")
else:
       print("not prime")
