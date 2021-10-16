##trying the join() function
list1= ['apple','banana', 'pinapple', 'guava']
print(list1)
str1= ', '.join(list1)
print(str1)

#using the split function:
list2= str1.split(',')
list3= str1.split(' ')
list4= str1.split('a')
print(' list2:',list2, '\n list3:',list3, '\n list4:', list4)

#using the partition function:
List2= str1.partition(',')
List3= str1.partition(' ')
List4= str1.partition('a')
print(' List2:',List2, '\n List3:',List3, '\n List4:', List4)


##Justifying string and Strip functions done directly.
