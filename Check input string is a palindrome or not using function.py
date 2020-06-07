#Write a function check_pal() that prints whether the input string is a palindrome or not. 
#A palindrome is a sequence of characters which reads the same backward as forward.
#The check should not be case-sensitive and should ignore blanks. 
#Expected outcome:
#check_pal("Barbara")
#Sorry, no palindrome!
#check_pal("Ana")
#Yes, palindrome indeed!
#check_pal("Never odd or even”)
#Yes, palindrome indeed!

print('Method 1')
text=str(input('Please Enter a Text')).lower().replace(" ","")

def check_pal(text):
  start=0
  stop=len(text)-1
  while (start<=stop):
    if text[start]!=text[stop]:
      print('Sorry, no palindrome!')
      return
    start+=1
    stop-=1
  print('Yes, palindrome indeed!')

check_pal(text)
print()


print('Method 2')
new_word=str(input('Please enter a word')).lower().replace(" ","")

def check_pal(new_word):  
  if new_word=="":
    return
    
  for n in range(len(new_word)):
    if new_word[n]!=new_word[(-1-n)]:
      print('Sorry, no palindrome!')
      return 
  print('Yes, palindrome indeed!')    
  
check_pal(new_word)
print()
