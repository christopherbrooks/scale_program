import os

os.remove("lily_scale.ly")

rhythmic_pattern = ('a', 3, 4)
scale = 'a b c des e fis g'
full_scale = ('acoustic', '1', 'c')

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

import webbrowser

#looking for a way to pop open a pdf reader
webbrowser.open_new(r'lily_scale.pdf')

