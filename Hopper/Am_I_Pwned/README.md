# Am I Pwned?
15 points

## Challenge 
> I was talking on IRC with a guy who tricked me into giving him a hash of my password and then said he could hack me! He said I might be “pwned”! I know the hashing algorithm is MD5; that’s still secure, right?

> … Oh, you want to know whether my password is secure or not?

> It doesn’t have any uppercase letters or numbers or punctuation, but isn’t six characters still a lot? what he meant by that one. Would you be able to hack my password? Here’s the hash:

> eca065fba51916821eb7274c786c67d9


## Hint
> The hacker told me that “MD5 is kinda rekt”. That sounds bad, right? I mean, how long would it take to brute force it…

## Solution

Easy find from https://crackstation.net

	Hash	Type	Result
	eca065fba51916821eb7274c786c67d9	md5	lmaoez

## Flag

	lmaoez