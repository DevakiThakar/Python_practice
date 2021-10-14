music = [0,1,2,3,4,5]
print(music, end='\n\n')

music[2] = music[0]
print(music)

lol= music*2
music = music + lol
print(music)
del music[5]
print(music)

for index, item in enumerate(music):
	print(str(index), item, sep='\t')



tup_1 = (0,1,2,3,4,5)

print(tup_1[2])

#tup_1[2] = 3
#del(tup_1[2])
