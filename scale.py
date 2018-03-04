from __future__ import division
import math
from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio
import random
import os

def scale(number_of_octaves):
# return notes for scale types
	scale = {'diatonic': [1 , 3, 5, 6, 8, 10, 12, 13], 
	'harm_maj': [1, 3, 5, 6, 8, 9, 12, 13], 
	'harm_min': [1, 3, 4, 6, 8, 9, 12, 13], 
	'acoustic': [1, 3, 5, 7, 8, 10, 11, 13],
	'hexatonic': [1, 2, 5, 6, 9 ,10, 13],
	'octatonic': [1, 2, 4, 5, 7, 8, 10, 11, 13],
	'whole tone': [1, 3, 5, 7 ,9 ,11, 13],
	'chromatic': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13] }

	types_of_scales = scale.keys()
	type_of_scale = random.sample(types_of_scales, 1)
	full_scale_list = scale.get(type_of_scale[0])
	
# scale can start on any note
	n = random.randint(0, len(full_scale_list) - 1)
	full_scale_list = full_scale_list[n:] + full_scale_list[1 : n]

# scale can be transposed to any octave
	k = random.randint(0, 12)
	for l in range(len(full_scale_list)):
		full_scale_list[l] = (full_scale_list[l] + k) % 12

# scale can have 1 through 4 octaves
	for i in range(1, number_of_octaves):
		full_scale_list = full_scale_list + full_scale_list
	full_scale_list = full_scale_list + full_scale_list[0 : 1]

#scale goes up and down
	full_scale_list = full_scale_list + full_scale_list[::-1]

# return frequency of tonic	
	frequencies = {
   0 : 130.81, # c
   1 : 138.59,  # c#, db
   2 : 146.83, # d
   3 : 155.56, # d# eb
   4 : 164.81, # e
   5 : 174.61, # f
   6 : 185.00, # f# gb
   7 : 196.00, # g
   8 : 207.65, # g# ab
   9 : 220.00, # a
   10 : 233.08, # a# bb
   11 : 246.94, # b
   12 : 261.63, } # c}

	tonic_frequency = frequencies[full_scale_list[0]]
	
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

# transform numbered steps to scale names
 	scale_spelled = []
 	n = 0
	while n < len(full_scale_list):
		scale_spelled.append(names[full_scale_list[n]])	
		n = n + 1

	return scale_spelled, tonic_frequency, type_of_scale[0]

# play a fixed frequency sound, used to sound tonic
def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    assert isinstance(frequency, float)
    assert isinstance(duration, int)

    n_samples = sample_rate * duration
    restframes = n_samples % sample_rate

    p = PyAudio()
    try:
        stream = p.open(format=p.get_format_from_width(1),  # 8bit
                        channels=1,  # mono
                        rate=sample_rate,
                        output=True)

        def s(t):
            wave = volume * math.sin(2 * math.pi * frequency * t / sample_rate)
            return int(wave * 0x7f + 0x80)

        full_range = range(0, n_samples, sample_rate)  # 0, n_samples, 2*n_samples, ... , sample_rate-1
        for i in full_range:
            partial_range = range(i, i + sample_rate)  # i, i+1, ..., i+sample_rate-1
            buf = map(s, partial_range)  # apply s to every int in partial range
            stream.write(bytes(bytearray(buf)))

        # fill remainder of frameset with silence
        stream.write(b'\x80' * restframes)
        
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

# generate rhythmic patterns and time signiture
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

	if beats_per_bar <= 3:
		beats_per_bar = beats_per_bar * 2

	return rhythmic_pattern, beats_per_bar, beat

# generate bowing patterns consisting of slurs and separate notes
# number of notes in bow pattern has to be even divisor of number of notes in scale
def slurs(scale):
	length_bow_pattern = random.randint(1, len(scale)-1) #slur pattern includes slured and separate notes
	while len(scale) % length_bow_pattern != 0:
		length_bow_pattern = random.randint(1, len(scale)-1)

# a bow pattern may or may not contain slurs
# slurs start with '[ ' any note can start a slur except the last in a bow pattern
# every '[ ' requires a '] ' any note can end a slur except the first in a bow pattern
	bow_pattern = []
	for k in range(length_bow_pattern):
		bow_pattern.append(random.randint(0,1))
		k += 1
 
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
			bow_pattern[k] = '( '
			begin_or_end = 'begin'
		elif  bow_pattern[k] == 1 and begin_or_end == 'begin':
			bow_pattern[k] = ') '
			begin_or_end = 'end'

	return bow_pattern

# Main Body of Program input number of octave and call scale function
while True:
	number_of_octaves = input("How many octaves?")
	if 0 < number_of_octaves <= 4:
		break

full_scale = scale(number_of_octaves)

#note that scale returns notes: full_scale[0] and frequency full_scale[1]
#get rhythms for scale
rhythmic_pattern = rhythm(full_scale[0])

#get slurs for scale
slurs = slurs(full_scale[0])

#add rhythms and slurs to scale
i = 1
while i < len(full_scale[0]):
	n = i % len(rhythmic_pattern[0])
	full_scale[0].insert(i, rhythmic_pattern[0][n])
	i += 2

# insert slurs
i = 2
while i < len(full_scale[0]):
	if n >= len(slurs):
		n = 0
	full_scale[0].insert(i , slurs[n])
	i += 3
	n += 1

scale = ''.join(full_scale[0])

print full_scale[2] #type of scale

# pitch of tonic
print full_scale[1]
sine_tone(full_scale[1], 3)

#format for lilypond and print
os.remove("lily_scale.ly")
lilyfile = open('lily_scale.ly', 'a') 
lilyfile.write('\\version \"2.18.2\" \n')
lilyfile.write("\\relative c' \n")
lilyfile.write('{ \n')
lilyfile.write('\\time \n')
lilyfile.write('{}/{} \n'.format(int(rhythmic_pattern[1]), rhythmic_pattern[2]))
lilyfile.write('{}\n'.format(scale))
lilyfile.write('} \n')
lilyfile.write('\\header { \n')
lilyfile.write('subtitle = \"{}, tonic: {}\"\n'.format(full_scale[2], full_scale[0][0]))
lilyfile.write('}')

lilyfile = open('lily_scale.ly', 'r')

print lilyfile.read()
lilyfile.close()

os.system("lilypond lily_scale.ly")

#op open a pdf reader
os.system("open lily_scale.pdf")
