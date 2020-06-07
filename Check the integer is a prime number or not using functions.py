#Write a function prime_check() that takes an integer as input and returns True if the integer is a prime number and False if it’s not. 
#A prime p is a natural number greater than 1 that only has 1 and itself as divisors. That is, only 1 and p divide p evenly.  
#prime numbers:example: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199 

print('Exercise 4')
def prime_check(number):
  if number>1:
    
    for num in range(2,number):
      if number%num==0:
        print(f'False, {number} is not a Prime number')
        return

    print(f'True, {number} is a Prime number')
    return

  else:
      print(f'False, {number} is not a Prime number')
  
prime_check(2)
prime_check(8)
prime_check(10)
prime_check(23)
prime_check(127)
