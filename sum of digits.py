a=int(input("enter the number"))
sum=0
while a>0:
    digit=a%10
    sum+=digit
    a//=10
print(sum)