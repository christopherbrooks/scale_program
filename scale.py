from __future__ import division
import math
from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio
import random

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
	print type_of_scale[0]
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
   1 : 130.81, # c
   2 : 138.59,  # c#, db
   3 : 146.83, # d
   4 : 155.56, # d# eb
   5 : 164.81, # e
   6 : 174.61, # f
   7 : 185.00, # f# gb
   8 : 196.00, # g
   9 : 207.65, # g# ab
   10 : 220.00, # a
   11 : 233.08, # a# bb
   12 : 246.94, # b
   13 : 261.63, } # c}

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

	return scale_spelled, tonic_frequency

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

# add rhthms

def rhythm(scale):
	rhythmic_subdivisions = {2: "2 ", 1.5: "4. ", 1.0: "4 ", 0.75: "8. ", 0.5: "8 ", 0.25: "16 "}

# generate rhythmic subdivision

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

#enter the rhythmic pattern into the scale
	print rhythmic_pattern
	print scale
	i = 1
	print len(scale)
	while i < len(scale):
		n = i % len(rhythmic_pattern)
		scale.insert(i, rhythmic_pattern[n])
		i += 2

	return scale

def slurs(scale):

	#needs some guts here
	return slurs

# Main Body of Program input number of octave and call scale function
while True:
	number_of_octaves = input("How many octaves?")
	if 0 < number_of_octaves <= 4:
		break
full_scale = scale(number_of_octaves)

#add rhythms to scale
full_scale = rhythm(full_scale[0])

#add slurs to scale

full_scale = slurs(full_scale)

# collapse into string to print to lilypond

scale = ''.join(full_scale)

beats_per_bar = 3
beat = 8

print '\\version \"2.18.2\"'
print "\\relative c'"
print '{'
print '\\time',
print '{}/{}'.format(int(beats_per_bar), beat)
print scale
print '}'

# pitch of tonic
print full_scale[1]
sine_tone(full_scale[1], 3)
