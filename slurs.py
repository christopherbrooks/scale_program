
import random



# generate bowing patterns

# number of notes in bow pattern has to be even divisor of number of notes in scale
def slurs(scale):
	length_bow_pattern = random.randint(1, len(scale)-1) #slur pattern includes slured and separate notes
	while len(scale) % length_bow_pattern != 0:
		length_bow_pattern = random.randint(1, len(scale)-1)

	print "lenght of bow pattern:", length_bow_pattern
# a bow pattern may or may not contain slurs
# slurs start with '[ ' any note can start a slur except the last in a bow pattern
# every '[ ' requires a '] ' any note can end a slur except the first in a bow pattern
	bow_pattern = []
	for k in range(length_bow_pattern):
		bow_pattern.append(random.randint(0,1))
		k += 1
 
	print len(bow_pattern)
#for l in range (len.bow_pattern):
	if len(bow_pattern) == 1:
		bow_pattern[0] = 0
	if sum(bow_pattern) % 2 == 1:
		bow_pattern[-1] = 0

	print bow_pattern

	begin_or_end = 'end' #slur
	for k in range(len(bow_pattern)):
		if bow_pattern[k] == 0:
			bow_pattern[k] = ' '
		elif  bow_pattern[k] == 1 and begin_or_end == 'end':
			bow_pattern[k] = '[ '
			begin_or_end = 'begin'
		elif  bow_pattern[k] == 1 and begin_or_end == 'begin':
			bow_pattern[k] = '] '
			begin_or_end = 'end'

	return bow_pattern
	

# main body of program
scale = ['a ', 'b ', 'c ', 'd ', 'ees ', 'f ', 'fis ', 'aes ', 'a ', 'b ', 'c ', 'd ']
scale = scale + scale[::-1]

print slurs(scale)



#enter the rhythmic pattern into the scale




