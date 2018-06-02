# Open Sourcery 2018
30 points

## Challenge 
> The solution to this problem lies within the Chromium source code. Literally. There is some string in there that mentions a flag and PACTF…

## Hint
> This problem builds off of a similarly named problem in PACTF 2017.

## Solution
 
Last year's solution involved some regex in the `transport_security_state_static.json` file.

(Look at the solution for [Open Sourcery 2017](https://writeups.amosng.com/2017/pactf_2017/boole/open-sourcery-2_40/) by @LFlare)

This year it is simpler: `Ctrl+F` or use `grep`.

	curl -s https://cs.chromium.org/codesearch/f/chromium/src/net/http/transport_security_state_static.json?cl=62089bc639bb3b5a5235583b7f19908f6d6ddc54
	| grep pactf

	    { "name": "pactf.com", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },
	    { "name": "impactfestival.be", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },
	    { "name": "pactf-flag-4boxdpa21ogonzkcrs9p.com", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },

## Flag

	pactf-flag-4boxdpa21ogonzkcrs9p.com
