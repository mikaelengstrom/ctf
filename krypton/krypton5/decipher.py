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


key = [0, 6, 12, -1, 6, -3, 4, 17, 3]
cipher = {
   'O': 'E',
   'D': 'T',
   'K': 'A',
   'Y': 'O', #
   'R': 'H',
   'C': 'S',
   'B': 'R',
   'S': 'I',
   'X': 'N',
   'V': 'L',
   'N': 'D',
   'P': 'F',
   'M': 'C', #
   'Q': 'G',
   'E': 'U',
   'G': 'W', #
   'W': 'M',
   'F': 'V',
   'L': 'B',
   'I': 'Y',
   'Z': 'P',
   'A': 'Q',
   'U': 'K',
   'H': 'X',
   'J': 'Z',
   'T': 'J'
}

def swap(c):
    return cipher[c.upper()]

with open('krypton6', 'r') as file:
    data = file.read().replace(' ', '')
    ##data = 'OICPIRKXLOICPIRKXL'
    row = ['', '']
    total = ''
    for c, pos in zip(data, cycle(range(0, 9))):
        diff = key[pos]
        letter_as_int = letter_to_int(c) + diff
        deciphered = swap(int_to_letter(letter_as_int))
        row[0] += deciphered + ' '
        row[1] += str(pos) + ' '
        total += deciphered

        if (pos is 8):
            print(row[0])
            #print(row[1])
            row = ['', '']

    print(row[0])
    print(total);
