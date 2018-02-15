from __future__ import division
import math
from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio
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
	
# scale can start on any note
	n = random.randint(0, len(full_scale_list) - 1)
	full_scale_list = full_scale_list[n:] + full_scale_list[1 : n]

# scale can have 1 through 4 octaves
	for i in range(1, number_of_octaves):
		full_scale_list = full_scale_list + full_scale_list
	full_scale_list = full_scale_list + full_scale_list[0 : 1]
# return frequency of tonic
	
	frequencies = {
   'c ': 130.81, 
   'cis ': 138.59,
   'des ': 138.59,
   'd ': 146.83,
   'dis ': 155.56,
   'ees ': 155.56,
   'e ': 164.81,
   'f ': 174.61, 
   'fis ': 185.00,
   'ges ': 185.00,
   'g ': 196.00,
   'gis ': 207.65,
   'aes ': 207.65,
   'a ': 220.00,
   'ais ': 233.08,
   'bes ': 233.08,
   'b ': 246.94,
   'c ': 261.63,
 }

	tonic_frequency = frequencies[full_scale_list[0]]
	#print full_scale_list[0]
	
	
	# print "tonic: ", scale.keys()

	#print full_scale_list
# returns scale as string
	full_scale = ''.join(full_scale_list)

	return full_scale, tonic_frequency


# play a fixed frequency sound
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


# Main Body of Program input number of octave and call scale function
while True:
	number_of_octaves = input("How many octaves?")
	if 0 < number_of_octaves <= 4:
		break
full_scale = scale(number_of_octaves)
# scale notes
print full_scale[0]
# pitch of tonic
sine_tone(full_scale[1], 3)