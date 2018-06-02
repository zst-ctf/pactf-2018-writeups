import hashlib
import sys

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

key = 'its?vIg'
plaintext = '4iyNz2zmshtmF_9ihyp'
cipher = xor(plaintext, repeat(key, len(plaintext)))
print(cipher)
