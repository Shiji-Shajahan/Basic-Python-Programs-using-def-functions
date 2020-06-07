#Write a function stats() that takes a list of numbers and prints some basic statistics. 
#Expected outcome:
#stats([3,11,18,20])
#basic statistics for list [3, 11, 18, 20]
#max value: 20 
#min value: 3
#length: 4
#sum: 52
#mean value: 13.0

print('Exercise 1')

def stats(numbers):
    print('max value is :',max(numbers))
    print('min value is :',min(numbers))
    print('length:',len(numbers))   
    print('sum:',sum(numbers))
    print('mean value',(sum(numbers)/len(numbers)))

stats([3,11,18,20])
