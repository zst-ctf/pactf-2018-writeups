# AI
80 points

## Challenge 
> Our artificial intelligence engineer made a groundbreaking discovery, but left the company unexpectedly… all we have is the obfuscated [source.txt…](source.dc0369d6de19.txt)

## Hint
> What language thinks 3 + ‘3’ == “33”?

## Solution

JSfuck language. It is obfuscated JavaScript. Paste the code into any Javascript interpreter and we see the text:

	"Congrats! You've uncovered the truth. Now go here: ibarakaiev.shpp.me/pactf_s7fj43/ai.zip"

This downloads a file `ai.zip`.

We see the following

	append_ai('The key is now stored securely in ("http://ibarakaiev.shpp.me/pactf_s7fj43/key_%d.txt", get_key_number(6, [16, 23, 16, 15, 42, 8])).', 30, 300);

	// this function returns the number needed to access key_%d.txt
	function get_key_number(n, arr) {
	    // TODO: implement solution to the following problem

	    /**
	     * You are given a sequence _s_ consisting of _N_ integers. You can divide it to 
	     * two sequences _p_ and _q_ such that every element of your sequence belongs exactly
	     * to one of these sequences. 
	     *
	     * Let _B_ be the sum of elements belonging to _p_, and _C_ be the sum of elements
	     * belonging to _C_. Note: if some of the sequences is empty then its sum is 0).
	     * What is the maximum possible value of _B_ - _C_ 
	     */
	}

In the function, it seems like we need to split up the array into `p` and `q` such that the `sum(p) - sum(q)` is minimised.

If you noticed, it says `sequences is empty then its sum is 0`. So it means that `q` can be empty. Hence the maximum sum is `sum(p) = sum(arr)`

	>>> sum([16, 23, 16, 15, 42, 8])
	120

Hence, we visit http://ibarakaiev.shpp.me/pactf_s7fj43/key_120.txt

Now we solve PACTFSCII by combining all the 5-bits into a binary string

	>>> charset = 'abcdefghijklmnopqrstuvwxyzPACTF '
	>>> text = 'mrxwozAp'
	>>> for ch in text:
	...   i = charset.index(ch)
	...   print(format(i, '05b'), end='')
	0110010001101111011001110110011101101111

Convert the binary string to ASCII and we have the flag


## Flag

	doggo
