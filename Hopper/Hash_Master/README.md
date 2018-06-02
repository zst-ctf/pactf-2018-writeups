# Hash Master
90 points

## Challenge 
> Miles forgot his login for [OPENWI:RE](https://openwi.re/), so he asked Darcy to send a password reset. Instead, she gave him the hash of his password—and the custom hashing algorithm. Miles doesn’t have great password security, so you could probably brute force it… but maybe there’s a way to do this more efficiently?

>Here is the hash of Miles’ password: `293366475`

>Here is the hashing algorithm:

	def hash_it(string):
	    q = 0
	    z = 127
	    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
	        q += i
	        z *= i
	    return (((q << 3)+1)*z) % (2**32 - 1)

## Hint
> Okay, [OPENWI:RE](https://openwi.re/) isn’t part of this problem. But you should still subscribe! If you’re interested in what else the PACTF team has been working on individually, check out [Miles’ personal site](https://rmrm.io/) and Igor’s [IcyBounce](https://icybounce.com/). Alex has been doing some [cool things too](https://reichenbach.org/).

> Oh, by the way, Miles’ shift keys don’t work—and he’s not a big fan of numbers.

## Solution

### Analysis

For the first char:

	Let index 0 be a

	q is the sum of ascii_codes.
	z is the 127 * product of ascii_codes.

	= ( ( (q << 3) + 1) * z ) % UINT_MAX
	= (8q + 1) * z % UINT_MAX
	= (8qz + z) % UINT_MAX

### Solving

From the hint, it is all lowercase letters

I tried using bruteforce. I did so with increasing char counts.

Having 1 to 5 chars took about 4 min to run, and then I arrived at 6 chars which got me the flag!

In actual fact, bruteforcing is really quick.

	$ python3 solve.py 
	aaaaaa 492652129623202831 1994267791 114704512
	aaaaab 498586041852171630 293366475 116086109
	solved! aaaaab

## Flag

	aaaaab