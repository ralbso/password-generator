# Needs optimization
# REVISE

def rotate(to_cipher, rot):
    '''
    to_cipher is the string we want to encode as a Caesar cipher
    rot is the amount of times the cipher is rotated

    to_cipher = str()
    rot = int()
    '''
    while rot >= 26:
        '''
        Reset number of rotations to 0 each time we reach z (letter 26)
        '''
        rot -= 26

    caesar = ''

    for char in to_cipher:
        '''
        For each char in the string, turn that into unicode values and sum
        the number of rotations, then convert it back to unicode.
        '''

        if ord(char) >= 97 and ord(char) <= 122: # Lowercase chars
            char = ord(char) + int(rot)

            if char > 122:      # If the sum surpasses z, return to a
                char = char - 26

            caesar += chr(char)         # Add ciphered chars onto the cipher string

        elif ord(char) >= 65 and ord(char) <= 90: # Uppercae chars
            char = (ord(char) + int(rot))

            if char > 90:       # if the sum surpasses Z, return to A
                char = char -26

            caesar += chr(char)

        else:
            caesar += char

    return caesar
