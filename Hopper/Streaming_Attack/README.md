# Streaming Attack
50 points

## Challenge 
> A popular `twitch.tv` streamer who goes by `BabblingBrook_PACTF` streams her adventures trying to visit a waterfall in every country that has one. She doesn’t like attention, so she encrypts her messages to us so that people don’t know where she’s heading next. I managed to get a copy of the encryption program, and I also managed to get an encrypted version of the message `TheCodeSamurai subscribed for 3 months!` sent to me by subscribing. Here’s the message (in hexadecimal):

`C1D7B5D06DD88D0F894E592B0A5FDB93C4F151C04BC2540D8626E5B0017D604E33ABC51334662B8ED8CCADE9B039AE4FB5F363EA9EDD32D551C32A892B058CDE8B0B`

Now, I want to decrypt the following message. Any way of helping me out?

`F4E0A7F276D99A3A894F40060245A48AC4E056FC58F4451C9063E2B22C323D3137B0D8382F7C6ECB`

[Here’s the encryption program; you’ll need it.](encryptor.ef241ed09dfc)

### Update

Streaming Attack has been updated. While the original version of the challenge is solvable, the updated version is clearer.

> ... the message `TheCodeSamurai subscribed for 3 months! Thank you, TheCodeSamurai!` sent to me by subscribing. ...

## Hint
> BabblingBrook_PACTF is a nice person, but I don’t think she’s super good at cryptography. Any way you could exploit that fact?


## Solution

Read up on [Stream Cipher Attacks](https://en.wikipedia.org/wiki/Stream_cipher_attacks)

	if anyone intercepts two messages encrypted with the same key, they can recover A xor B

So if we XOR the 2 encrypted texts, and then XOR with the 1st plaintext, we will get the 2nd plaintext.

	$ python3 solve.py 
	a_waterfall_is_just_a_stream_on_its_side

## Flag

	a_waterfall_is_just_a_stream_on_its_side