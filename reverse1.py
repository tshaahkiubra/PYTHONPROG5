num=int(input("enter a number:"))
rev_num=0
rem=0
while (num>0):
       rem=num%10
       rev_num=(rev_num*10)+rem
       num=num//10
print('the reversed number is :{}'.format(rev_num))      
