scale = [8, 10, 11, 2, 3, 5, 7]
print scale

# note names with more common accidentals
names = {
   0 : 'c ', # c
   1 : 'cis ',  # c#, db
   2 : 'd ', # d
   3 : 'ees ', # d# eb
   4 : 'e ', # e
   5 : 'f ', # f
   6 : 'fis ', # f# gb
   7 : 'g ', # g
   8 : 'aes ', # g# ab
   9 : 'a ', # a
   10 : 'bes ', # a# bb
   11 : 'b ', # b
   12 : 'c ', # c
 }

alternate_accidentals = {
   1 : 'des ',  # c#, db
   3 : 'dis ', # d# eb
   6 : 'get ', # f# gb
   8 : 'gis ', # g# ab
   10 : 'ais ', # a# bb
 }

n = 0
scale_spelled = []
while n < len(scale):
	scale_spelled.append(names[scale[n]])
	if scale_spelled[n][0] == scale_spelled[n - 1][0]:
		print scale_spelled[n]
		#scale_spelled[n] = alternate_accidentals[n]
		print "what about them damn accidentals?"
	n = n + 1

print scale_spelled
