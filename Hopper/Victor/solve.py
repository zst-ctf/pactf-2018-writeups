#!/usr/bin/env python3

header = '1340628579'
rows = {
    ' ': 'АОП#СНЕГ##',
    '0': 'БВДЖЗИЙКЛМ',
    '7': 'РСТУФХЦЧШЩ',
    '9': 'ЬЮЯ_Э     ',
}

message = '7264160199640987865519282923616105'
secret = ('12261991'*len(message))[:len(message)]

# reverse secret addition operation
ciphertext = ''
for m, s in zip(message, secret):
    digit = int(m) - int(s)
    if (digit < 0):
        digit += 10
    ciphertext += str(digit)
    assert 0 <= digit <= 9


def getchar(number):
    number = number.rjust(2)
    assert len(number) == 2, number

    row = rows[number[0]]
    ch_index = header.index(number[1])

    return row[ch_index]


if __name__ == '__main__':
    number = ''
    output = ''
    while len(ciphertext) > 0:
        # get one digit
        number += ciphertext[:1]
        ciphertext = ciphertext[1:]
        # look up digit
        ch = getchar(number)
        if ch == '#':
            continue
        else:
            number = ''
            output += ch
    print(output)
