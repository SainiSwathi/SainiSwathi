#3. Write a python program finding the factorial of a given number using a while loop. 


n=int(input('Enter a number: '))
fact = 1
for n in range(1, n+1):
     fact*=n
print (f'{n}!={fact}')
