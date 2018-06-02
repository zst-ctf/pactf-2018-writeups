#!/usr/bin/env python3
import string

UINT_MAX = (2**32 - 1)
def hash_raw(string):
    q = 0
    z = 127
    ascii_codes = [int(byte) for byte in bytearray(string, "utf-8")]
    for i in ascii_codes:
        q += i
        z *= i
    return ( ( (q << 3) + 1) * z )


def attempt(string):
    raw = hash_raw(string)
    hash = raw % UINT_MAX
    k = raw // UINT_MAX
    print(string, raw, hash, k)

    if (hash == 293366475):
        print("solved!", string)
        quit()


if __name__ == '__main__':
    #main()
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    for e in string.ascii_lowercase:
                        for f in string.ascii_lowercase:
                            attempt(a + b + c + d + e + f)
