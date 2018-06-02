# Zip Zap Zop
45 points

## Challenge 
> My friend gave me this [file](download.zip), but I have no idea what to do with it?

## Hint
> I tried to make this file really, really small.

## Solution

This is a zlib compressed file

	$ file download.zip 
	download.zip: zlib compressed data

It can be decompressed using pigz

	$ pigz -d -z --stdout download.zip > output1.zip

Upon decompressing, it produces another zlib file.

Make a bash script to recursively decompress until done.

	$ bash solve.sh 
	Decompressed 1 times
	Decompressed 2 times
	...
	Decompressed 66 times
	pigz: skipping: output67.zip unrecognized format

	$ file output67.zip 
	output67.zip: data

	$ strings output67.zip 
	flagq
	Gotza_Makes_1T_V_small_1539511106q


## Flag

	Gotza_Makes_1T_V_small_1539511106
