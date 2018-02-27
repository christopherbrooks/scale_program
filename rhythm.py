
import random


def rhythm(scale):
	rhythmic_subdivisions = {2: "2 ", 1.5: "4. ", 1.0: "4 ", 0.75: "8. ", 0.5: "8 ", 0.25: "16 "}

# number of notes in rhythmic subdivision has to be even divisor of number of notes in scale
	number_of_notes = random.randint(1,8)

	while len(scale) % number_of_notes != 0:
		number_of_notes = random.randint(1,8)
	
	rhythmic_pattern = []
	pattern_duration = 0

	for l in range(number_of_notes):
		k = random.randint(0, len(rhythmic_subdivisions)-1)
		note_value = rhythmic_subdivisions.values()[k]
		rhythmic_pattern.append(note_value)
		note_duration = rhythmic_subdivisions.keys()[k]
		pattern_duration = pattern_duration + note_duration

# figure time signature

	while pattern_duration % .5 != 0:
		pattern_duration += pattern_duration

	if pattern_duration % 1 == 0:
		beats_per_bar = pattern_duration
		beat = 4
	elif pattern_duration % .5 == 0:
		beats_per_bar = pattern_duration * 2
		beat = 8
	else:
		beats_per_bar = pattern_duration * 4
		beat = 16

	return rhythmic_pattern, beats_per_bar, beat



scale = ['a ', 'b ', 'c ', 'd ', 'ees ', 'f ', 'fis ', 'aes ', 'a ']
#scale = scale + scale[::-1]

print rhythm(scale)






