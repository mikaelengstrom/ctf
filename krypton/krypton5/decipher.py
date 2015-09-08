from itertools import cycle

alphabet = "abcdefghijklmnopqrstuvwxyz"
def letter_to_int(c):
    return alphabet.index(c.lower())

def int_to_letter(int):
    while int >= len(alphabet):
        int -= len(alphabet)
    while int < 0:
        int += len(alphabet)
    return alphabet[int]


key = [0, -12, 1, -5, 1, 7]
cipher = {
    'J': 'E', 
    'Y': 'T', 
    'T': 'O', 
    'M': 'H', 
    'W': 'R', 
    'F': 'A', 
    'X': 'S',
    'S': 'N', 
    'I': 'D',
    'N': 'I',
    'Q': 'L', 
    'B': 'W',
    'K': 'F', 
    'Z': 'U',
    'H': 'C', 
    'D': 'Y',
    'L': 'G',
    'R': 'M',
    'U': 'P',
    'P': 'K', #
    'G': 'B',
    'A': 'V',
    'O': 'J',
    'C': 'X', 
    'E': 'q',
    'V': 'z',
}

def swap(c):
    return cipher[c.upper()]

with open('found2', 'r') as file:
    data = file.read().replace(' ', '')
    #data = 'JVIOIC'
    row = ['', '']
    total = ''
    for c, pos in zip(data, cycle(range(0, 6))):
        diff = key[pos]
        letter_as_int = letter_to_int(c) + diff
        deciphered = swap(int_to_letter(letter_as_int))
        row[0] += deciphered + ' '
        row[1] += str(pos) + ' '
        total += deciphered

        if (pos is 5):
            print(row[0])
            #print(row[1])
            row = ['', '']

    print(row[0])
    print(total);
