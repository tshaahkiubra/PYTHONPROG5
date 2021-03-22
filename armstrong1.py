num=int(input("enter a number:"))
sum=0
temp=num
digit=0
ln=len(str(num))
while temp>0:
       digit=temp%10
       sum=sum+(digit**ln)
       temp=temp//10
if num==sum:
       print(num,"is an Armstrong number")
else:
       print(num,"is not an Armstrong number")
       
       
