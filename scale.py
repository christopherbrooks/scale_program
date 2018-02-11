# defines the notes of a scale
import random

def scale(number_of_octaves):
# return notes for scale types
	scale = {'diatonic': ['c ', 'd ', 'e ', 'f ', 'g ', 'a ', 'b ', 'c '], 
	'harm_maj': ['c ', 'd ', 'e ', 'f ', 'g ', 'aes ', 'b ', 'c '], 
	'harm_min': ['c ', 'd ', 'ees ', 'f ','g ', 'aes ', 'b ','c '], 
	'acoustic': ['c ', 'd ', 'e ', 'fis ', 'g ', 'a ' 'bes ', 'c '],
	'hexatonic': ['c ', 'des ', 'e ', 'f ', 'gis ' ,'a ','c '],
	'octatonic': ['c ', 'des ', 'ees ' 'e ', 'fis ', 'g ', 'a ', 'bes ', 'c '],
	'whole tone': ['c ', 'd ', 'e ', 'fis ' ,'gis ' ,'ais ', 'c '],
	'chromatic': ['c ','cis ', 'd ' ,'ees ', 'e ', 'f ', 'fis ' ,'g ' ,'gis ' ,'a ' ,'bes ' ,'b ' ,'c '] }

	types_of_scales = scale.keys()
	type_of_scale = random.sample(types_of_scales, 1)
	print type_of_scale[0]
	full_scale_list = scale.get(type_of_scale[0])
	full_scale = ''.join(full_scale_list)

# scale can start on any note
	n = random.randint(0, len(full_scale) - 2)
	print n
	if n % 2 == 0: # n is even
		full_scale = full_scale[n:] + full_scale[2: n + 1]
	else: #n is odd
		full_scale = full_scale[n + 1:] + full_scale[2: n + 2]

# scale can have 1 through 4 octaves
	if number_of_octaves == 0:
		return full_scale
	else:
		for i in range(1, number_of_octaves):
			full_scale = full_scale + full_scale [1:]

	return full_scale

# input number of octave and call scale function
while True:
	number_of_octaves = input("How many octaves?")
	if 0 < number_of_octaves <= 4:
		break
print number_of_octaves
print scale(number_of_octaves)