import sys
import random
sys.path.insert(0, './Python-random-module-cracker')
from randcrack import RandCrack

rc = RandCrack()

with open('input_file.txt', 'r') as f:
    input_lines = f.read().splitlines()

for i, lines in enumerate(input_lines):
    number = int(lines)
    if i < 624:
        rc.submit(number)
    else:
        prediction = rc.predict_randrange(0, 4294967295)
        assert prediction == number

prediction = rc.predict_randrange(0, 4294967295)

print(f"Flag: {prediction}")
