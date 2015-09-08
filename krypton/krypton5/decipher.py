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
    'J': 'e', #
    'Y': 't', #
    'T': 'o',
    'M': 'h',
    'W': 'l',
    'F': 'a',
    'X': 'i',
    'S': 'n',
    'I': 'd',
    'N': 's',
    'Q': 'm',
    'B': 'u',
    'K': 'c',
    'Z': 'r',
    'H': 'w',
    'D': 'f',
    'L': 'y',
    'R': 'g',
    'U': 'p',
    'P': 'b',
    'G': 'v',
    'A': 'k',
    'O': 'j',
    'C': 'x', #
    'E': 'q',
    'V': 'z',
}

def swap(c):
    return cipher[c.upper()]

with open('found1', 'r') as file:
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
