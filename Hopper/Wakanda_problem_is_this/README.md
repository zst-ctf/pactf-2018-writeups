# Wakanda problem is this?
60 points

## Challenge 
> You’ve arrived at Wakanda’s border. Only the flag will allow you to enter. [This is all you have.](gate.5ae2b2e0aa79.jpg)

## Hint
> Use the bytes in the second image.

## Solution

There's hidden files in a ZIP file

	$ strings gate.5ae2b2e0aa79.jpg | tail -5
	Pm|yf
	3n64E-
	xv|5
	blackpanther1.jpgPK
	blackpanther2.jpgPK
	Wakanda_problem_is_this $ 

Use formost

	# foremost gate.5ae2b2e0aa79.jpg 

We get the file `00000058.zip` which has 2 images. The hint mentions bytes, lets compare the files. 

	$ cmp -l blackpanther1.jpg blackpanther2.jpg  | gawk '{printf "%c", strtonum(0$3)}' 
	flag{wakanda4eva}

(Similar to [Diff in EasyCTF 2018](https://github.com/zst123/easyctf_iv-2018-writeups/tree/master/Solved/Diff))

## Flag

	wakanda4eva
