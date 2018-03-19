scale = ['bes ', 'd ', 'e ', 'f ', 'g ', 'aes ', 'b ', 'c ']
tonic = scale[0]
print tonic

frequencies = dict(
   c=130.81,
   cis=138.59,
   des=138.59,
   d=146.83,
   dis=155.56,
   ees=155.56,
   e=164.81,
   f=174.61,
   fis=185.00,
   ges=185.00,
   g=196.00,
   gis=207.65,
   aes=207.65,
   a=220.00,
   ais=233.08,
   bes=233.08,
   b=246.94,
   # c=261.63  # why do you have 2 c's?
 )

print frequencies[tonic]
