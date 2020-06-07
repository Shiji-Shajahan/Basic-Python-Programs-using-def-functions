print("Function def")
a=4
b=3
if a%b==0:
  print(a,"is evenly divisible by",b,"\n")
else:
  print(a,"is not evenly divisible by",b,"\n")

c=8
d=4
if c%d==0:
  print(c,"is evenly divisible by",d,"\n")
else:
  print(c,"is not evenly divisible by",d,"\n")
print()  

#built in python functions
print("hallo")
list=[3,4]
result=sum(list)
print(result)
help(print)
len(list)
max(list)

def check_divisibility(number1,number2):
  if number1%number2==0:
    print(number1,"is evenly divisible by",number2,"\n")
  else:
    print(number1,"is not evenly divisible by",number2,"\n")

check_divisibility(4,3)
check_divisibility(8,4)
check_divisibility(9,3)
print()

def check_divisibility1(number1,number2):
  if number1%number2==0:
    print(number1,"is evenly divisible by",number2,"\n")
  else:
    print(number1,"is not evenly divisible by",number2,"\n")

check_divisibility1(int(input('enter first number')),int(input('enter second number')))
print()  

#function without parameters
def func():
  print("hello")

func()

def basic_operations():
  print("hello")
  a=3
  b=10
  c=a+b
  print(c)

basic_operations()

#similar function with parameters
def basic_operations(name):
  print("hello",name)
  a=3
  b=10
  c=a+b
  print(c)

basic_operations("shiji")

#function within another function
def operation(name):
  print("hello",name)
  a=3
  b=10
  c=a+b
  print(c)
  listi=[3,4]
  print(sum(listi))

operation("shiji")
print()

#function with return order of parameters matters  
def difference(a,b):
  c=a-b
  return c

result=difference(4,5)
print(result)
result=difference(5,4)
print(result)
result=difference(a=5,b=4)
print(result)

def f(x):
  if x<0:
    return
  elif x>100:
    return
  print("number is neither <0 and >100")

f(8)


#Guess the output 1
def func1(number1, number2):
    total = number1 + number2
    print(total)
    
func1(2, 4)

#Guess the output 2
def func2(number1, number2):
    total = number1 + number2
    print(total)
    
total_from_function = func2(2, 4)
print(total_from_function)

#Guess the output 3
def func3(number1, number2):
    total = number1 + number2 
    return total
    
total_from_function = func3(2, 4)
print(total_from_function)

#Guess the output 4
def func4(number1, number2):
    return number1 + number2
    
total_from_function = func4(2, 4)
print(total_from_function)

# global vs. local variables:

# global variables outside of function
a = 10
print(a)

# global var. accessible inside and outside of functions 
def func():
  print("inside the function")
  print(a)

func()

# local variable defined inside function will not affect global one
def func2():
  print("local variable in function")
  a = 5
  print(a)

func2()
# global variable still has same value
print("after function call")
print(a)

# to use local variable ouside of function we have to return it
def func3():
  a = 5 + 234 + 3 / 23 + 234 * 1324
  return a

result = func3()
print("print result returned from function")
print(result)


