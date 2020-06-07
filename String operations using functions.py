#1. Write a function list_benefits() that returns a list with the following strings:
#“More organized code”
#“More readable code”
#“Easier code re-use”
#“Allowing programmers to share and connect code together”

print("Question 1")

def list_benefits():
  str1="More organized code"
  str2="More readable code"
  str3="Easier code re-use"
  str4="Allowing programmers to share and connect code together"
  codes1=[str1,str2,str3,str4]
  return codes1
  
codes2=list_benefits()
print('codes2=',codes2)
print()

#2. Write a function build_sentence() which receives a string and returns a sentence starting with the given string and ending with the string “is a benefit of functions!”

#Exercise 3 Q2

def build_sentence(str8):
  
  str9="is a benefit of functions!"
  return (str8+" "+str9)


#3. Copy the following function name_the_benefits_of_functions() to the same code and call it to see how the functions work together!
#def name_the_benefits_of_functions():
    #list_of_benefits = list_benefits()
    #for benefit in list_of_benefits:
        #print(build_sentence(benefit))

print("Exercise 3 Q3")        
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#print(build_sentence(benefit)) will add benefit or the elements in list_of_benefits to str9 in built_sentence(str8)
