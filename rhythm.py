
import random

scale = ['a ', 'b ', 'c ', 'd ', 'ees ', 'f ', 'fis ', 'aes ', 'a ']
scale = scale + scale[::-1]

print len(scale)

print scale

rhythmic_subdivisions = {2: "2 ", 1.5: "4.5 ", 1.0: "4 ", 0.75: "8. ", 0.5: "8 ", 0.25: "16 "}

# generate rhythmic subdivision

# number of notes in rhythmic subdivision has to be even divisor of number of notes in scale
number_of_notes = random.randint(1,8)

while len(scale) % number_of_notes != 0:
	number_of_notes = random.randint(1,8)
	

rhythmic_pattern = []

for l in range(number_of_notes):
	k = random.randint(0, len(rhythmic_subdivisions)-1)
	note_value = rhythmic_subdivisions.values()[k]
	rhythmic_pattern.append(note_value)

print rhythmic_pattern







