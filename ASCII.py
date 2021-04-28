
SEQ = '005TD'

LETTER = bytes(SEQ, 'utf-8')

# Addind the next letter
nextLetter = str(bytes([LETTER[4] + 1]))

# Convert byte to str
LETTER = str(LETTER[0:5])

print('Current: ' + LETTER[2:-1])
print('Next Sequence: ' + LETTER[2:-2] + nextLetter[2])