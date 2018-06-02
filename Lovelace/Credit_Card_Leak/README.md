# Credit Card Leak
35 points

## Challenge 
> ShoeShop was hacked, and all of their customer records were released online—including credit card numbers. One credit card in the leak is invalid, however. What is the invalid credit card number?

> Here’s the leak: [cc_leak.txt.bz2](cc_leak.txt.eecc6f896436.bz2)

## Hint
> The credit card numbers in the leak are obviously all invalid, but most would pass a certain credit card validity test. All credit card numbers except one, that is.

## Solution

Let's use this credit card library to check validity of the numbers.

- https://github.com/joshleeb/creditcard


	$ python3 solver.py 
	8692015931457397
	Done.


## Flag

	8692015931457397