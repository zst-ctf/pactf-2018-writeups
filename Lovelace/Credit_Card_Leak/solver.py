#!/usr/bin/env python3
from creditcard import luhn

numbers = open('cc_leak.txt', 'r').read()

for card_no in numbers.splitlines():
	if not luhn.is_valid(card_no):
		print(card_no)

print('Done.')
