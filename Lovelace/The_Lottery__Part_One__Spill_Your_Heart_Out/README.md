# The Lottery, Part One: Spill Your Heart Out!
65 points

## Challenge 
> I was playing this [lottery](output.81ed5b400225). Which number is going to win next time? If only you could see into the future…

## Hint
> Brought to you by Oracle Corporation! Spill your heart out!


## Solution

Java random number generator (Read: `Oracle Corporation`).

Hence, it has to do with finding the next value given 2 numbers in the sequence.

I found this:

https://crypto.stackexchange.com/questions/51686/how-to-determine-the-next-number-from-javas-random-method

Modify the code to fit our needs

	$ javac solve.java
	$ java solve
	Starting
	Seed found: -135594114706202
	So we have that nextInt is: -1997362081 and 
	the third one is: -632232200 with seed: -135594114706202


## Flag

	-632232200