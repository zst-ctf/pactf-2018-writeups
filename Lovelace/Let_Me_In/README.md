# Let Me In
20 points

## Challenge 
> You received this [account.rar](account.5a52b336da78.rar) file, but it is ‘protected’ under a password. Can you break in?

## Hint
> Something tells me the user might not be using complex passwords…

## Solution

### Failed
Resources on RAR crackers:

	https://github.com/jaredsburrows/rarcrack
	http://www.crark.net/#download
	https://3583bytesready.net/2016/02/17/building-john-the-ripper-1-8-0-jumbo-on-mac-os-10-11-el-capitan/
	https://gist.github.com/reggi/2faadedd925789a3d25196f2a036ecc6
	http://easymactips.blogspot.sg/2011/06/how-to-install-john-ripper-on-mac.html
	http://openwall.info/wiki/john/johnny#Binary-redistributables

Initially, I thought of bruteforcing (above crackers), but it yielded no results...


### Successful

Then, I decided to use password lists...

	$ wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

I coded a simple unrar iterator in bash, only to find out that the first entry is the password... (Gah, wasted my time)

	$ bash bruteforce.sh 
	Password is: 123456

And the password extracts a file, `flag.txt`...

	$ cat flag.txt 
	rgSueiMYehWJSZPZr

## Flag

	rgSueiMYehWJSZPZr
