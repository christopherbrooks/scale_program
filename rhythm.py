import random


def rhythm(scale):
    rhythmic_subdivisions = {2: 2, 1.5: 4., 1.0: 4, 0.75: 8., 0.5: 8, 0.25: 16}

    # number of notes in rhythmic subdivision has to be even divisor of number of notes in scale
    divisors = [i for i in range(1, 8) if len(scale) % i == 0]
    number_of_notes = random.choice(divisors)

    random_choices = random.sample(rhythmic_subdivisions.items(),
                                   number_of_notes)
    """
    zip converts `[(a, 1), (b, 2), ...]` to `([a, b, ...], [1, 2, ...])`
    `f(*[a, b, c])` means `f(a, b, c)`. In other words, `*` tells a function
    to treat every element of the input as a separate argument
    """
    rhythmic_pattern, durations = zip(*random_choices)
    rhythmic_pattern = [random.choice(rhythmic_subdivisions)
                        for _ in range(number_of_notes)]
    pattern_duration = sum(durations)

    # figure time signature

    while pattern_duration % .5 != 0:
        pattern_duration += pattern_duration

    multiple = 1 if pattern_duration % 1 == 0 else 2
    beats_per_bar = rhythmic_pattern * multiple
    beat = 4 * multiple
    return rhythmic_pattern, beats_per_bar, beat


scale = ['a ', 'b ', 'c ', 'd ', 'ees ', 'f ', 'fis ', 'aes ', 'a ']
# scale = scale + scale[::-1]

print rhythm(scale)
