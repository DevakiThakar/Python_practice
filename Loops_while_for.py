i=1
while i <5:
    print('Devaki' , i)
    i+= 1
    n= i%3
    if n==0:
        print(i, 'fish', n,  'sheep')
        
    elif i> 3:
        continue
    else:
        break

for i in range (0,15, 2):
    print(i)

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
j =4
for i in days:
    print ('date is ', j, 'Oct, and the day is ', i)
    j+=1
import random

for i in range (9):
    print(random.randint(1,10))
