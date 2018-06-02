# The Lottery, Part Two: Untwisting Fate!
90 points

## Challenge 
> This time the lottery is harder than ever! Can you manage to untwist the cockles of fate itself? Can you see into the future?

> [They seem to have given me a lot more information. Perhaps it’ll help?](output.9327e404be0e)


## Hint
> We may regard the present state of the universe as the effect of its past and the cause of its future. An intellect which at a certain moment would know all forces that set nature in motion, and all positions of all items of which nature is composed, if this intellect were also vast enough to submit these data to analysis, it would embrace in a single formula the movements of the greatest bodies of the universe and those of the tiniest atom; for such an intellect nothing would be uncertain and the future just like the past would be present before its eyes. — Pierre Simon Laplace, A Philosophical Essay on Probabilities


## Solution

From the information, it uses Python's PRNG to generate 1000 unsigned 32-bit integers.

As a background, [Python PRNG is using Mersenne Twister](https://github.com/james727/MTP).

I tried using these references to solve it butit didn't really work:
- https://github.com/altf4/untwister
- https://tailcall.net/blog/cracking-randomness-lcgs/

---

Eventually, I found this which worked without an issue!
- https://github.com/tna0y/Python-random-module-cracker

I made a script which submits 624 numbers, then predicts until it reaches 1001.

The 1001st number is our flag!

	$ git clone https://github.com/tna0y/Python-random-module-cracker
	$ python3 solver.py 
	Flag: 3956993139

## Flag

	3956993139