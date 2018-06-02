import wave
import struct
import math
import re
import binascii
import array

# https://stackoverflow.com/a/5281240

audible = wave.open('bits-filtered.wav', 'r')

print("Audio Information")

# get information
length = audible.getnframes()
frequency = audible.getframerate()
print("> Length:", length)
print("> Frequency:", frequency)

# extract data
print("Extracting WAV data")
waveData = []
for i in range(0, length):
    waveData.append(audible.readframes(1))
    print(f"\r> Done {i}", end='')
print("\r> Done all")

# for each step, calculate average value
print("Averaging amplitude values")

step = int(frequency * 0.469)  # read every 0.469 sec
threshold = 900
print("> Interval:", step)
print("> Threshold:", threshold)

amplitudes = []
position = 0
while position < length:
    total_value = 0
    for i in range(step):
        if position >= length:
            break

        # parse the data and add amplitude to sum
        data = struct.unpack("<h", waveData[position])
        position += 1

        # skip first and last 10% of the frame
        # prevent noise from entering the data
        #if (i < (step * 0.1)) or (i > (step * 0.9)):
        #    continue

        value = int(data[0])
        total_value += abs(value)        

    # average out the value over each step
    total_value /= step
    print(">", total_value)
    amplitudes.append(total_value)

# parse to binary based on threshold
output = ''
for amplitude in amplitudes:
    if amplitude > threshold:
        output += '1'
    else:
        output += '0'

msg = binascii.unhexlify('%x' % int(output, 2))
print(msg.decode())
