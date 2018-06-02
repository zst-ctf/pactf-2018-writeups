#!/usr/bin/env python3
import binascii
from PIL import Image

img = Image.open('true-blue.08c0cb787f26.png').convert('RGB')
pixels = img.load()
width, height = img.size

output = ''
for y in range(0, height // 6):
	for x in range(0, width):
		r, g, b = pixels[x, y]
		output += '1' if (r & 0x01 == 1) else '0'
		output += '1' if (g & 0x01 == 1) else '0'
		output += '1' if (b & 0x01 == 1) else '0'
		# print(pixels[x, y])

msg = binascii.unhexlify('%x' % int(output, 2))
print(msg.decode(errors='ignore'))
