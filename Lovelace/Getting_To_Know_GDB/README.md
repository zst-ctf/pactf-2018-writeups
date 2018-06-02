# Getting To Know GDB
50 points

## Challenge 
> A friend sent me a [mysterious binary](mysterious_elf.771c3c9447cd). It’s supposed to print out the flag, but it’s giving me a weird poem and some hex instead.


## Hint
> The flag is in there somewhere, but something gives me the feeling that searching the binary for strings wont help…


## Solution

When we run the program, it gives lots of random base64 strings.

	$ ./mysterious_elf.771c3c9447cd 
	This is the string you're allowed to see...
	  It is here for viewing, no matter what your intention may be...

	But something more interesting below this sea...
	  Fortunately for you, there is such a thing as GDB!

	The solution is simple, but you have been baited...
	  For the println that reveals the flag has been truncated!

	The flag was in there, all ready to go–but not anymore...
	  Now all that remains is some random base 64!

	The flag is:
	 --> YUtLSDhhUVVSMWI0cGFhVQ== <--^C


Let's look at the decompiled code in Hopper. 

Look at `main` or `binary::main::hf421c7ec894951b1` label:

	loc_4aae:

    xmm0 = intrinsic_movaps(xmm0, *(int128_t *)"why_use_breakpoints_if_you_have_");
    arg_19 = intrinsic_movaps(arg_19, xmm0);
    xmm0 = intrinsic_movaps(xmm0, *(int128_t *)0x238f0);
    arg_21 = intrinsic_movaps(arg_21, xmm0);
    stack[2014] = 0x67;
    stack[2015] = 0x6f;
    stack[2015] = 0x6f;
    stack[2015] = 0x64;
    stack[2015] = 0x5f;
    stack[2015] = 0x74;
    stack[2015] = 0x69;
    stack[2015] = 0x6d;
    stack[2015] = 0x69;
    stack[2016] = 0x6e;
    stack[2016] = 0x67;
    stack[2016] = *(int8_t *)rbx;
    stack[2020] = *0x23b20;
    xmm0 = intrinsic_movdqu(xmm0, *(int128_t *)const.1m);
    arg_27 = intrinsic_movdqa(arg_27, xmm0);
    rax = base64::encode::encoded_size::h43525f70931340cd(&arg_7, 0x2c, &arg_27, rcx, r8);
    if (arg_7 == 0x0) goto loc_60ab;

Parse the inline-chars

	>>> x = [0x67, 0x6f, 0x6f, 0x64, 0x5f, 0x74, 0x69, 0x6d, 0x69, 0x6e, 0x67]
	>>> ''.join(list(map(lambda y: chr(y), x)))
	'good_timing'

This gives us the string

	why_use_breakpoints_if_you_have_good_timing

*Note: I can't seem to solve it using GDB breakpoints though...*

## Flag

	why_use_breakpoints_if_you_have_good_timing