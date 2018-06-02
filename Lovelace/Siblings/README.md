# Siblings
120 points

## Challenge 
> One 4096-bit RSA key is impossible to break, so 20 must be even better! By chaining each encryption together, surely it’s impossible for you to figure out what the message is?

> [Everything you’ll need (except the private keys, you’re on your own for that!)](problem-data.e34ba61084c2.zip)

## Hint
> Numbers don’t have siblings, right? What could that mean?

## Solution

Siblings mean that the numbers are related some how...

Take a look at the keys and we find that in all the keys, the exponent is always 65537.

	public_keys $ openssl rsa -pubin -inform PEM -text -noout -in key0.pem 

This means that the modulus (`n`) are related.

---

Refer to this article: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Importance_of_strong_random_number_generation

	They exploited a weakness unique to cryptosystems based on integer factorization. If n = pq is one public key and n′ = p′q′ is another, then if by chance p = p′ (but q is not equal to q'), then a simple computation of gcd(n,n′) = p factors both n and n′, totally compromising both keys

Hence, if there exists some gcd between all the numbers, they can be factorised.

---

Now we have the factors, we read from `encoding_method.md` on how to decrypt it

	I feel confident enough about my encoding that I'll tell you exactly how I did it! The public keys
	folder has keys numbered 0 through 19. I simply encoded the bytes of a message (in big-endian
	order), applied key 0, key 1, and so on until key 19. The message is basic ASCII: I'll tell you that
	much.

So we decrypt from key 19 to key 0 and then read the bytes in big endian form.

--- 

Put all into a script and we get the flag

	$ python3 solve.py 
	t00 many c00ks sp0il the br0th


## Flag

	t00 many c00ks sp0il the br0th
