# Third Eye
40 points

## Challenge 
> Sometimes​‌‌‌​‌‌‌​‌‌​ there‌​​​​‌‌​​​​‌ is ​‌‌‌​‌​​​‌​‌‌‌more ‌‌​‌‌​​‌​‌​‌‌​‌‌​​​‌‌‌​​‌‌​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​‌‌​​​‌‌‌​‌​‌​‌‌‌​​‌​​‌‌​‌​‌‌​‌‌‌​​‌‌​‌​‌‌‌‌‌​‌‌​​​‌than ​​‌‌​​‌​‌​‌‌​‌‌meets ‌​​‌‌​​‌​‌​‌‌​​​the ​‌​‌‌‌​‌​​​‌‌​‌​​​​‌​‌‌‌‌‌​‌‌‌eye​‌​​​‌‌​‌​​​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​​‌​‌​‌‌‌‌​​‌​‌‌​​‌​‌.

## Hint
> Maybe if you just squint harder…

## Solution

Inspect elements on the challenge description.

We see this in HTML.

	<div class="problem-description">
		<p>Sometimes&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203; there&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj; is &#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;more &zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;than &#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;meets &zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;the &#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;eye&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;.</p>
	</div>

Remove all text and leave behind the `&#8203` and `&zwnj;`. Then convert to binary string.

	>>> x = '&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&zwnj;&#8203;&#8203;&#8203;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;&zwnj;&#8203;&#8203;&zwnj;&#8203;&zwnj;'

	>>> x.replace('&#8203;', '1').replace('&zwnj;', '0')
	'10001000100101111001111010001011101000001001101010010011100011001001101010100000100100111000101010001101100101001000110010100000100111011001101010010001100110101001111010001011100101111010000010001011100101111001101010100000100110101000011010011010'

	>>> x.replace('&#8203;', '0').replace('&zwnj;', '1')
	'01110111011010000110000101110100010111110110010101101100011100110110010101011111011011000111010101110010011010110111001101011111011000100110010101101110011001010110000101110100011010000101111101110100011010000110010101011111011001010111100101100101'

The latter is the correct one, giving us the flag

## Flag

	what_else_lurks_beneath_the_eye