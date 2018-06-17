lower=150
upper=160
for n in range(lower, upper + 1):
orde =len(str(n))
    sum=0
temp=n
   while(temp > 0):
       digit=temp % 10
       sum+=digit ** order
       temp //=10
   if (n==sum):
       print(num)


