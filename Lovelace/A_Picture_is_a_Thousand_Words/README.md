# A Picture is a Thousand Words
10 points

## Challenge 
> Apparently there is something hidden in this [image…](image.d25eefefc427.jpg)

## Hint
> You’re looking for text—how might you look at the text of the image?

## Solution

There's lots of `c`s being printed in `strings`. Don't get confused, it is simpler than that.

	 $ strings *.jpg | grep 'flag'
	flag_is_DjKVIXXQRZZrrAd


## Flag

	DjKVIXXQRZZrrAd