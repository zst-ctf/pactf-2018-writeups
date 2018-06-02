# Reversal 3 2 1
50 points

## Challenge 
> I received [this file](source.6d9692804a8b.out) from my bananagrams partners! I think they’re just trying to distract me from the game. I need to finish this one quick, so I can get back to my game! Any help?

## Hint
> Who doesn’t like a good game of bananagrams?


## Solution

Run the program

	$ ./source.6d9692804a8b.out 
	$H*+R4.\=_

Decompile the main in Hopper

	int main(int arg0, int arg1) {
	    var_54 = arg0;
	    var_60 = arg1;
	    var_8 = *0x28;
	    rax = 0x0;
	    var_40 = 0x24;
	    var_3C = 0x5;
	    var_38 = 0x48;
	    var_34 = 0x2a;
	    var_30 = 0x2b;
	    var_2C = 0xe;
	    var_28 = 0x52;
	    var_24 = 0x34;
	    var_20 = 0x2e;
	    var_1C = 0x17;
	    var_18 = 0x5c;
	    var_14 = 0x3d;
	    var_10 = 0x5f;
	    for (var_44 = 0x0; var_44 <= 0xc; var_44 = var_44 + 0x1) {
	            rax = putchar(*(int32_t *)(rbp + sign_extend_32(var_44) * 0x4 + 0xffffffffffffffc0));
	    }
	    rax = putchar(0xa);
	    rax = 0x0;
	    rdx = *0x28 ^ *0x28;
	    if (rdx != 0x0) {
	            rax = __stack_chk_fail();
	    }
	    return rax;
	}

What we see when we run the program

	>>> str += chr(0x24);
	>>> str += chr(0x5);
	>>> str += chr(0x48);
	>>> str += chr(0x2a);
	>>> str += chr(0x2b);
	>>> str += chr(0xe);
	>>> str += chr(0x52);
	>>> str += chr(0x34);
	>>> str += chr(0x2e);
	>>> str += chr(0x17);
	>>> str += chr(0x5c);
	>>> str += chr(0x3d);
	>>> str += chr(0x5f);
	>>> str
	'$\x05H*+\x0eR4.\x17\\=_'
	>>> print(str)
	$H*+R4.\=_


We see functions `bananagrams0` through `bananagrams99`. Seeing the first few in Hopper, there's a lot to "reverse" engineer.

	// 0x400cf4: "%d\n"
	// 0x400cf8: "g:"

	int bananagrams0() {
	    var_4 = 0x2;
	    goto loc_4005fa;

	loc_4005fa:
	    if (var_4 * var_4 <= 0x2) goto loc_4005e7;

	loc_400606:
	    rax = printf("%d\n");
	    return rax;

	loc_4005e7:
	    rax = 0x2 % var_4;
	    if (rax == 0x0) {
	    	return rax;
	    } else {
	    	var_4++;
	    }
	}

	void bananagrams1() {
	    rsp = rsp + 0x8;
	    rbp = stack[2047];
	    return;
	}
	void bananagrams2() {
	    rsp = rsp + 0x8;
	    rbp = stack[2047];
	    return;
	}

For example, the first few will print some string

	bananagrams0: print "2\n"
	bananagrams3: print "4\n"
	bananagrams5: print "g:"

Let's use GDB to call all 100 of these functions. I'll use pwntools to do so.

	$ python gdb-bruteforce.py > result.txt

Afterwhich, filter those logging messages to get the raw strings

	$ cat result.txt | grep -Ev "^(\[\*\])"
	[x] Starting local process '/usr/bin/gdb'
	[+] Starting local process '/usr/bin/gdb': pid 115
	2
	4
	g:2
	_a_byte__9172
	flaambled_9101
	102__108_10_1042
	scr902__104_102askjndlfalsfjlkfs_10421


	$ cat result2.txt | grep -Ev "^(\[\*\])" | grep -Ev "^\\$" | grep -Ev "^$"
	[x] Starting local process '/usr/bin/gdb'
	[+] Starting local process '/usr/bin/gdb': pid 309
	2
	4
	g:
	2
	_a_byte_
	_917
	2
	fla
	amble
	d
	_910
	1
	102_
	_108
	_10
	_104
	2
	scr
	902_
	_104
	_102
	askjndlfalsfjlkfs
	_1042
	1

Reverse?

	>>> '24g:2_a_byte__9172flaambled_9101102__108_10_1042scr902__104_102askjndlfalsfjlkfs_10421'[::-1]
	'12401_sfkljfslafldnjksa201_401__209rcs2401_01_801__2011019_delbmaalf2719__etyb_a_2:g42'

Not sure if this is the right track, can't seem to solve using any combination

## Flag

	??