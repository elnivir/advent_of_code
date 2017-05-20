import string


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

with open('zad4.txt', 'r') as dane:
    for line in dane:
        temp = line.replace('-', '').replace(']', '').split('[')

        wnk = caesar(temp[0][:-3], ((int(temp[0][-3:])) % 26))
        if wnk[:5] == "north":
            print(wnk, temp[0][-3:])
