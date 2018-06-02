# Security Through Obscurity?
50 points

## Challenge 
> We intercepted this message, but we can’t make heads or tails of it. It was rattled off so fast, too… How could anyone be that good at using a cipher?

>Anyway, here’s the message. Good luck!

	Tązhii, Łį́į́ʼ, Dzeeh Mąʼii, Dibé yázhí, Wóláchííʼ, Tłʼízí Tin, Dibé Mósí, Łį́į́ʼ, Dzeeh, Dibé, Tązhii, Dzeeh, Gah, Neeshchʼííʼ, Dzeeh, Béésh dootłʼizh

## Hint
> This definitely doesn’t look like English. What else could it be? Perhaps looking through the history books might help…

## Solution

Search the message online and we find [this code by @TheZ3ro, credits to him](https://gist.github.com/TheZ3ro/572ef81c0f20bf9c4c435b32a62a7056).

Modify it for our text and we get the output:

	$ python3 navajo.py
	THEFLAGISCHESTERNEZ

## Flag

	CHESTERNEZ