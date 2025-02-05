#3. Python program to check if a given number is an Armstrong number

n=int(input('Enter the number: '))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**b)
    n=n//10
if s==sum1:
    print("armstrong number")
else:
    print("Not a armstrong number")





















