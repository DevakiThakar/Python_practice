def what(i):
    print('what did you say,' +i+ '?')
    print('i did not hear you, ' +i)
    print(i+ 'i beg your pardon?')

what('bob')



def simpleInterest(amount,rate,year):
    return amount*rate*year/100

print ('Amount', 'Interest', sep='\t', end='\n\n')
for i in range (5):
    n= simpleInterest((i*500),3,2)
    print ( i*500, n, sep='\t' )
