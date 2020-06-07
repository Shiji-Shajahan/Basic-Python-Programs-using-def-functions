#A recursive function is a function that calls itself again during its execution.
#def func1(n):
#    return n * func1(n-1)

#Make the code above work so that the function calculates factorials of integers, e.g. 
#3! = 3 x 2 x 1
#4! = 4 x 3 x 2 x 1

print('Exercise 6')
def func1(n):
  if n==0:
    return 1
  elif n==1:
    return 1
  else:
    return (n * func1(n-1))

n=int(input("Please Enter a number"))
print(f'Factorial of {n} is :',func1(n))


