
#making a trial dictionary on favourite fruits of different people
fave_frt = {
    'raghav': 'apple',
    'devaki': 'orange',
    'mukta': 'peach',
    'sudeep': 'kiwi',
    'piya':'banana',
    'cortana': 'starfruit'
    }
'''#to print all the people and their favourite fruits:
for i in fave_frt.keys():
    j=fave_frt[i]
    print('the favourite fruit of', i, 'is :', j)

#stating the favourite fruits of the people the user inputs, and asking for the fave fruit incase its not in the dictionary:

while True:
    print ('enter name:')
    name= input()

    if name=='':
        break
    elif name in fave_frt:
        print('the fave fruit of ', name, 'is ', fave_frt[name])
    else:
        print('this persons data isnt available, please enter their favourite fruit:')
        fave_frt[name]= input()

##using get() to retrieve values:
#which fruit does raghav like?
print(fave_frt.get('raghav', 'no fruits'))
'''
## setting defaults:
fave_frt.setdefault('chris', 'pineapple')
while True:
    print ('enter name:')
    name= input()

    if name=='':
        break
    elif name in fave_frt:
        print('the fave fruit of ', name, 'is ', fave_frt[name])
    else:
        print('this persons data isnt available, please enter their favourite fruit:')
        fave_frt[name]= input()
