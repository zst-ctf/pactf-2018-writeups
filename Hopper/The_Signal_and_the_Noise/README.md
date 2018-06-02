# The Signal and the Noise
35 points

## Challenge 
> There’s a message in here somewhere! You’ll have to find it yourself.

> [Find the needle in the haystack!](haystack.ef77fe451087.txt)


## Hint
> There must be something that distinguishes the signal from the noise. How could you mark something in a plain text file? All you have are Unicode characters…

## Solution

`All you have are Unicode characters` means there's some hidden message in unicode characters.

Showing non-alphanumeric words, they are

	b'th\xe2\x80\x8de'
	b'fla\xe2\x80\x8cg'
	b'i\xe2\x80\x8bs'
	b'i\xef\xbb\xbfn'
	b'p\xef\xbb\xbflain'
	b'sigh\xef\xbb\xbft'
	b'

Join these together and we get the flag

## Flag

	the flag is in plain sight