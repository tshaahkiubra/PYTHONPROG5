num=int(input("enter a number:"))
i=1
while (i<=num):
       if i%5==0:
              if i%2==0:
                     continue
              print(i,end=" ")
       i=i+1
