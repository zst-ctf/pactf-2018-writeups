#!/usr/bin/env python3
from Crypto.PublicKey import RSA

'''
https://gist.github.com/JonCooperWorks/5314103

Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Mod-inverse code by ofaurax
#     https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m


def main():
    # read in the keys
    modulus = []
    for i in range(20):
        f = open(f'./static/public_keys/key{i}.pem','r')
        key = RSA.importKey(f.read())
        modulus.append(key.n)

    factors = dict()
    # check gcd between every possible pair of the keys
    for i1 in range(20):
        for i2 in range(20):
            if (i1 == i2):
                continue
            n1 = modulus[i1]
            n2 = modulus[i2]

            divisor = gcd(n1, n2)
            if divisor != 1:
                # factorise
                p = divisor
                q1 = (n1 // divisor)
                q2 = (n2 // divisor)
                # make sure the factors are correct
                assert int(p * q1) == n1
                assert int(p * q2) == n2
                # store into our dictionary
                factors[i1] = (p, q1)
                factors[i2] = (p, q2)
                '''
                print(f"p{i1}: {p}")
                print(f"q{i1}: {q1}")
                print(f"p{i2}: {p}")
                print(f"q{i2}: {q2}")
                '''

    # now decrypt from 19 to 0
    ciphertext = open(f'./static/unbreakable_code','rb').read()

    for i in reversed(range(20)):
        n = modulus[i]
        e = 65537
        p, q = factors[i]
        phi = (p - 1) * (q - 1)
        d = modinv(e, phi)

        priv_key = RSA.construct((n, e, d, p, q))
        ciphertext = priv_key.decrypt(ciphertext)

    message = ciphertext.decode()
    print(message)

if __name__ == '__main__':
    main()
