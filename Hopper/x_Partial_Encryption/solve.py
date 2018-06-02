#!/usr/bin/env python3
import string
import pyDes

KEY = "its?vIg"
CIPHERTEXT = "4iyNz2zmshroBc9kmtm"
'''
for ch in string.printable:
	key = KEY.replace('?', ch)
	des = pyDes.des(key)
	plaintext = des.decrypt(CIPHERTEXT)
	print(plaintext)

'''
from Crypto.Cipher import AES

def main():
    for ch in string.printable:
        key = KEY.replace('?', ch)
        cipher = AES.new(key, AES.MODE_ECB)
        ptext = cipher.decrypt(CIPHERTEXT)
        print(f"{key}: {ptext}")

if __name__ == '__main__':
    main()

