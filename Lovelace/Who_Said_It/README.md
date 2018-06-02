# Who Said It?
25 points

## Challenge 

	-----BEGIN PGP SIGNED MESSAGE-----
	Hash: SHA512

	The Internet Research Agency (IRA) (Агентство интернет-исследований), also known as Glavset[2] and known in Russian Internet slang as the Trolls from Olgino or kremlebots, is a Russian company, based in Saint Petersburg, engaged in online influence operations on behalf of Russian business and political interests. The agency has employed fake accounts registered on major social networks, discussion boards, online newspaper sites, and video hosting services in order to promote the Kremlin's interests in domestic and foreign policy including Ukraine and the Middle East as well as attempting to influence the 2016 United States presidential election. More than 1,000 employees reportedly worked in a single building of the agency in 2015.
	-----BEGIN PGP SIGNATURE-----

	iQIzBAEBCgAdFiEEpwC3NwnaBW1k5jyITNA/bv0j4ekFAlqwTv0ACgkQTNA/bv0j
	4elTZBAAwPnCem0Zq75MGYR2TFeIq4Sgc1jHIoL9sc/LQQDNvTcd58nZ0VO1P0hg
	IPEuybypNM00hVADSfilP+B/CpuGmvzuuNdbi2Ikc7wKjiPl8+FO0Koa3PsXZpqS
	y6dozKacdqR7y53A7j1vhC5jv7ZX94xeRad5PQ6PjLAKZc6JTshNhy69RRr7Sf/P
	LlfA0JFDG6evEJ+BDKUuQeDcoLqT082eSdFLtN6XhF0aMOawlEBEgnIvPV8sdR0F
	w8+FJntSivAKRxgSlqkaeAqLRJbCI2EKoimxUAIerQwzJMWPk3e36mizvqoshrE6
	vuxZdEUxX4OUuQumbTe4tYkNbVCsqCFDbLrOLemSfVmazAIgfxoxgH5XYhhP2adz
	cV+4v9U/6U6x9ebiiVdW/K7mbrkjro9Nv71+JfJNZuAHq97lufbRUuhIPudXT45s
	hlvw8Yt7qn/SNfkr5qtfYLslhRW40F7bWHrzEdtCfzkh7H0sqzaqVDEogt/BcSC1
	O8ZZLyaq3Vab6FfDch/2B7rmQihmFj59c5zj0Oy69cNW1mipQrrSV3i2jHc1U1GM
	RRQiQzJ6GS3FVJ7L2hcBMUYfVyRWnfpCUS8kpW4TPOtIhFYJ/0gixd82g2P2MdNa
	0kyphm0fZktbunW9IeNjsvQf6SNiMOJZ5V4OEjSzPJMa5HNbj38=
	=Dn7K
	-----END PGP SIGNATURE-----

## Hint
> Keys live on keyservers.

## Solution

Reference:
- https://security.stackexchange.com/questions/62916/can-i-get-a-public-key-from-pgp-signature

See verbose output from GPG

	$ cat message.txt | gpg -vv

	gpg: WARNING: no command supplied.  Trying to guess what you mean ...
	gpg: armor: BEGIN PGP SIGNED MESSAGE
	gpg: armor header: Hash: SHA512
	# off=0 ctb=ff tag=63 hlen=2 plen=19 new-ctb
	:packet 63: length 19 - gpg control packet# off=21 ctb=cb tag=11 hlen=2 plen=0 partial new-ctb
	gpg: armor: BEGIN PGP SIGNATURE
	:literal data packet:
		mode t (74), created 0, name="",
		raw data: unknown length
	gpg: original file name=''
	The Internet Research Agency (IRA) (Агентство интернет-исследований), also known as Glavset[2] and known in Russian Internet slang as the Trolls from Olgino or kremlebots, is a Russian company, based in Saint Petersburg, engaged in online influence operations on behalf of Russian business and political interests. The agency has employed fake accounts registered on major social networks, discussion boards, online newspaper sites, and video hosting services in order to promote the Kremlin's interests in domestic and foreign policy including Ukraine and the Middle East as well as attempting to influence the 2016 United States presidential election. More than 1,000 employees reportedly worked in a single building of the agency in 2015.
	# off=804 ctb=89 tag=2 hlen=3 plen=563
	:signature packet: algo 1, keyid 4CD03F6EFD23E1E9
		version 4, created 1521503997, md5len 0, sigclass 0x01
		digest algo 10, begin of digest 53 64
		hashed subpkt 33 len 21 (issuer fpr v4 A700B73709DA056D64E63C884CD03F6EFD23E1E9)
		hashed subpkt 2 len 4 (sig created 2018-03-19)
		subpkt 16 len 8 (issuer key ID 4CD03F6EFD23E1E9)
		data: [4096 bits]
	gpg: Signature made Tue Mar 20 07:59:57 2018 +08
	gpg:                using RSA key A700B73709DA056D64E63C884CD03F6EFD23E1E9
	gpg: Can't check signature: No public key

Lookup the KeyID (which is `4CD03F6EFD23E1E9`) on the MIT Public Key Server 

> http://pgp.mit.edu/pks/lookup?op=get&search=0x4CD03F6EFD23E1E9

Now we can save the public key and get the details!

	$ gpg solved.txt 
	gpg: WARNING: no command supplied.  Trying to guess what you mean ...
	pub   rsa4096 2018-03-19 [SC]
	      A700B73709DA056D64E63C884CD03F6EFD23E1E9
	uid           Oxford Automata (the_real_answer_is_always_in_the_comments) <oxfordautomata@sendmiles.email>
	sub   rsa4096 2018-03-19 [E]


## Flag

	the_real_answer_is_always_in_the_comments