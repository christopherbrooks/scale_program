scale = [8, 10, 11, 2, 3, 5, 7]
print scale

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

alternate_accidentals = {
    1: 'des ',  # c#, db
    3: 'dis ',  # d# eb
    6: 'get ',  # f# gb
    8: 'gis ',  # g# ab
    10: 'ais ',  # a# bb
}

n = 0
scale_spelled = [names[s] for s in scale]
for n in range(len(scale)):
    if scale_spelled[n][0] == scale_spelled[n - 1][0]:
        print scale_spelled[n]

print scale_spelled
