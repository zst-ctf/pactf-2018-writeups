#!/usr/bin/env python3

x = bytes.fromhex('C1D7B5D06DD88D0F894E592B0A5FDB93C4F151C04BC2540D8626E5B0017D604E33ABC51334662B8E')
y = bytes.fromhex('F4E0A7F276D99A3A894F40060245A48AC4E056FC58F4451C9063E2B22C323D3137B0D8382F7C6ECB')

def xor_bytes(xs, ys):
    return bytes((x ^ y) for x, y in zip(xs, ys))

a_xor_b = xor_bytes(x, y)

a = "TheCodeSamurai subscribed for 3 months! Thank you, TheCodeSamurai! ".encode()
b = xor_bytes(a_xor_b, a)

print(b.decode())
