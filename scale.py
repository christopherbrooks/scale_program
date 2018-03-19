from __future__ import division
import math
from pyaudio import PyAudio  # sudo apt-get install python{,3}-pyaudio
import random
import os

from print_to_lilypond import write_lilypond
from rhythm import rhythm
from slurs import slurs
from tone_generator import sine_tone


def scale(number_of_octaves):
    # return notes for scale types
    scale = dict(diatonic=[1, 3, 5, 6, 8, 10, 12, 13],
                 harm_maj=[1, 3, 5, 6, 8, 9, 12, 13],
                 harm_min=[1, 3, 4, 6, 8, 9, 12, 13],
                 acoustic=[1, 3, 5, 7, 8, 10, 11, 13],
                 hexatonic=[1, 2, 5, 6, 9, 10, 13],
                 octatonic=[1, 2, 4, 5, 7, 8, 10, 11, 13],
                 whole_tone=[1, 3, 5, 7, 9, 11, 13],
                 chromatic=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    type_of_scale = random.choice(scale)
    full_scale_list = scale[type_of_scale]

    # scale can start on any note
    n = random.randrange(len(full_scale_list))
    full_scale_list = full_scale_list[n:] + full_scale_list[:n]

    # scale can be transposed to any octave
    k = random.randrange(12)
    full_scale_list = [(note + k) % 12 for note in full_scale_list]

    # scale can have 1 through 4 octaves
    full_scale_list *= number_of_octaves
    full_scale_list += full_scale_list[:1]

    # scale goes up and down
    full_scale_list += full_scale_list[::-1]

    # return frequency of tonic
    frequencies = [
        130.81,  # c
        138.59,  # c#, db
        146.83,  # d
        155.56,  # d# eb
        164.81,  # e
        174.61,  # f
        185.00,  # f# gb
        196.00,  # g
        207.65,  # g# ab
        220.00,  # a
        233.08,  # a# bb
        246.94,  # b
        261.63]  # c}

    tonic_frequency = frequencies[full_scale_list[0]]

    # note names with more common accidentals
    names = [
        'c ',  # c
        'cis ',  # c#, db
        'd ',  # d
        'ees ',  # d# eb
        'e ',  # e
        'f ',  # f
        'fis ',  # f# gb
        'g ',  # g
        'aes ',  # g# ab
        'a ',  # a
        'bes ',  # a# bb
        'b ',  # b
        'c ',  # c
    ]

    # transform numbered steps to scale names
    scale_spelled = [names[n] for n in full_scale_list]
    return scale_spelled, tonic_frequency, type_of_scale


# Main Body of Program input number of octave and call scale function
while True:
    number_of_octaves = input("How many octaves?")
    if 0 < number_of_octaves <= 4:
        break

scale_spelled, tonic_frequency, type_of_scale = scale(number_of_octaves)

# note that scale returns notes: full_scale[0] and frequency full_scale[1]
# get rhythms for scale
rhythmic_pattern = rhythm(scale_spelled)
rhythmic_pattern_, beats_per_bar, beat = rhythmic_pattern

# get slurs for scale
slurs = slurs(scale_spelled)

# add rhythms and slurs to scale
for i in range(0, len(scale_spelled), 2):
    n = i % len(rhythmic_pattern_)
    scale_spelled.insert(i, rhythmic_pattern_[n])

# insert slurs
for n in range(0, len(scale_spelled)):
    if n >= len(slurs):
        n = 0
    scale_spelled.insert(n * 3, slurs[n])

scale = ''.join(scale_spelled)

print type_of_scale  # type of scale

# pitch of tonic
print tonic_frequency
sine_tone(tonic_frequency, 3)

write_lilypond(beats_per_bar, beat, scale_spelled, type_of_scale)
