# Go Git It
25 points

## Challenge 
> The code samurai (also known by his pseudonym Nicholas) was making some final optimizations on his program when… he accidentally decapitated it.

> Download the samurai’s repository: [go git it.tar.bz2](go_git_it.tar.427f1b62f4aa.bz2)

## Hint
> Perhaps ‘chopping a branch off a tree’ would be the more precise analogy.

## Solution

Untar and we get a git repo which is up-to-date

However, if we look at the last commit, there's something fishy.

	WaveFunctionCollapse $ cat .git/logs/HEAD 
	0000000000000000000000000000000000000000 fad1066b5000f7e9fbda0ef81bbea56799686670 Miles McCain <milesmcc@users.noreply.github.com> 1523062635 -0400	clone: from https://github.com/mxgmn/WaveFunctionCollapse.git
	fad1066b5000f7e9fbda0ef81bbea56799686670 116ec4958d68f844d480f50c2bd4dcbe6aa0b909 Miles McCain <milesmcc@users.noreply.github.com> 1523062652 -0400	checkout: moving from master to 116ec4958d68f844d480f50c2bd4dcbe6aa0b909
	116ec4958d68f844d480f50c2bd4dcbe6aa0b909 01ab3947246a08dcddf71056c330473bbb58d0ed Miles McCain <milesmcc@users.noreply.github.com> 1523062721 -0400	commit: I AM THE CODE SAMURAI
	01ab3947246a08dcddf71056c330473bbb58d0ed fad1066b5000f7e9fbda0ef81bbea56799686670 Miles McCain <milesmcc@users.noreply.github.com> 1523062728 -0400	checkout: moving from 01ab3947246a08dcddf71056c330473bbb58d0ed to master

There seems to be a hidden/deleted commit `01ab3947246a08dcddf71056c330473bbb58d0ed` with the commit message `I AM THE CODE SAMURAI`.

We can access it and get the contents

	$ pigz -d < .git/objects/01/ab3947246a08dcddf71056c330473bbb58d0ed 
	commit 266tree 1655d9f332295ef7dc50dd0aac7d3f51fffd982a
	parent 116ec4958d68f844d480f50c2bd4dcbe6aa0b909
	author Miles McCain <milesmcc@users.noreply.github.com> 1523062721 -0400
	committer Miles McCain <milesmcc@users.noreply.github.com> 1523062721 -0400

	I AM THE CODE SAMURAI


Let's revert to that commit!

	WaveFunctionCollapse $ git checkout 01ab3947246a08dcddf71056c330473bbb58d0ed
	Note: checking out '01ab3947246a08dcddf71056c330473bbb58d0ed'.

Now, we can see the commit...


	WaveFunctionCollapse $ git log
	commit 01ab3947246a08dcddf71056c330473bbb58d0ed (HEAD)
	Author: Miles McCain <milesmcc@users.noreply.github.com>
	Date:   Fri Apr 6 20:58:41 2018 -0400

	    I AM THE CODE SAMURAI

	commit 116ec4958d68f844d480f50c2bd4dcbe6aa0b909
	Author: Wandmalfarbe <Wandmalfarbe@users.noreply.github.com>
	Date:   Sun Oct 2 14:59:43 2016 +0200

	    Corrected some spelling mistakes in README.md

	commit 333f592b6612da43ec475c988c09325378c662e9
	Author: mxgmn <maxgumin@protonmail.ch>
	Date:   Fri Sep 30 16:41:09 2016 +0400

	    link typo

	commit 05b692d8cad58319cc448418081916a84e3ee6be
	Author: mxgmn <maxgumin@protonmail.ch>
	Date:   Fri Sep 30 15:06:40 2016 +0400

	    typos


Let's take a look at the diff of the commit.

	WaveFunctionCollapse $ git show 01ab3947246a08dcddf71056c330473bbb58d0ed
	commit 01ab3947246a08dcddf71056c330473bbb58d0ed (HEAD)
	Author: Miles McCain <milesmcc@users.noreply.github.com>
	Date:   Fri Apr 6 20:58:41 2018 -0400

	    I AM THE CODE SAMURAI

	diff --git a/README.md b/README.md
	index 3ee1001..b5fff7b 100644
	--- a/README.md
	+++ b/README.md
	@@ -107,3 +107,5 @@ Some samples are taken from the games Ultima IV and [Dungeon Crawl](https://gith
	 
	 <p align="center"><img alt="second collage" src="http://i.imgur.com/CZsvnc7.png"></p>
	 <p align="center"><img alt="voxel perspective" src="http://i.imgur.com/RywXCHn.png"></p>
	+
	+The flag is `3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad`!


## Flag

	3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad