#Write a function even_elements() that takes a list of integers and returns a list containing the even elements of the input list. 
#Expected outcome:
#list_even = even_elements([3,4,5,6,7,11,12,13,14])
#print(list_even)
#[4, 6, 12, 14]

print("Exercise 2")
even_numbers=[]

def even_elements(numbers):
  for i in numbers:
    if i%2==0:
      even_numbers.append(i)
  return even_numbers

list_even = even_elements([3,4,5,6,7,11,12,13,14])
print('The list of even numbers is:',list_even)

