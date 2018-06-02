# Letter to a Machine
25 points

## Challenge 
> You intercepted a letter.rar—but to read it, you have to prove that you are _not a human_. The password is `NOT BAD` + `FACE`.


## Hint
> I’m sure it’s just coincidence that `BAD` and `FACE` can be spelled with just the letters `ABCDEF`…


## Solution

Spelled with `ABCDEF` probably means it is some hex string.

After some guessing, `NOT` means the unary-NOT or complement operator.

Hence, let's do the following

	void main() {
	    printf("%X", ~0xBAD + 0xFACE);
	}

This prints our RAR password
	
	EF20

Unzip it and we get the flag

## Flag

	lIZORZaOkWrIuNB