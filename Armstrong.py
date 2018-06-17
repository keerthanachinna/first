n= int(input("enter a number: "))
 length=len(str(n))
sum=0
temp=n
 while(temp!=0):
    sum=sum+((temp % 10)**length)
    temp=temp 
 
if (sum==n):
    print("yes armstrong number")
else:
    print("not armstrong number")
