import os


def write_lilypond(beats_per_bar, beat, scale_spelled, type_of_scale):
    os.remove("lily_scale.ly")

    with open('lily_scale.ly', 'a') as lilyfile:
        lilyfile.write('\\version \"2.18.2\" \n')
        lilyfile.write("\\relative c' \n")
        lilyfile.write('{ \n')
        lilyfile.write('\\time \n')
        lilyfile.write('{}/{} \n'.format(beats_per_bar, beat))
        lilyfile.write('{}\n'.format(scale))
        lilyfile.write('} \n')
        lilyfile.write('\\header { \n')
        lilyfile.write('subtitle = \"{}, tonic: {}\"\n'.format(type_of_scale, scale_spelled))
        lilyfile.write('}')

    with open('lily_scale.ly', 'r') as lilyfile:
        print lilyfile.read()

    os.system("lilypond lily_scale.ly")

    # op open a pdf reader
    os.system("open lily_scale.pdf")


if __name__ == '__main__':
    # rhythmic_pattern = ('a', 3, 4)
    # full_scale = ('acoustic', '1', 'c')
    scale = 'a b c des e fis g'
    write_lilypond(3, 4, 'acoustic', scale)
