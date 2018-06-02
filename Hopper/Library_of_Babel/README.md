# Library of Babel
75 points

## Challenge 
> Is this what passes through fiber optic cables? Must be…


## Hint
> It is much faster to extract frames from the video and write a script!


## Solution

Extract qrcode frames

	$ mkdir qrcode
	$ ffmpeg -i video.f3db89aeb9f4.mp4 "qrcode/out-%03d.png"

Parse QR codes using zbarimg

	$ cd qrcode
	$ for file in *.jpg; do echo "$file"; zbarimg $file; done > ../output.txt

Alternatively, I tried [this convenient Docker container](https://github.com/int32bit/qrcode), but it gave some corrupted strings...

	$ cd frames
	$ for file in *.jpg; do docker run -t -i --rm -v `pwd`:/root krystism/qrcode decode --file $file; done > ../output.txt
	

In the output, we see this

	=== YOUR ANSWER IS HERE ===
	"eqvzb" w-3, s-5, v-25, p-248
	22syz7u9dogitfxlezobhobeuno6pnec20n6bqfg22cqihe41hbbi8aut4t618oj4wee4to32mdfmmsykl76r002hfbsurum4rr6tprxi4yinrzlqee17y5sfw11k5ybxsie6icu2x6fxvbq2wskzjtmng31ejzfikwj9ql0nxutriwr6p6vqzpdl1thkgt0o4is7znam9xub632v5mi39t8oae98kv5faatt11zitxmuka8qdrhbyw02i89fx9desufb6giwvgsvgrd18925zrgrqai31l92i6qplb9embayx8gmhqczl4gi9mb112plzs78w38hhbqmximi718hte6tw6b2m42xfwh3nnby2jemn0sz80hevqccfpyqd674swckdyaaptdp482x25uanhh5q8r0xqtokgwb8lbn41vl4mhhfvoeippvnl1t3ojshstgwumk48q8l3m937sou6b1838u7pie8da6gh8d8q5e09vazbdpsbtwyu35we0vu1r9cxfsaeisivqa01nrols0xculnijghh4goztt2ymrt2h54hfbg8o5w03ai9ghobywjxxd8erazpyjisdnrehi3xvh6yz6gnynrsgbzek9uv2poyrdld0quk3cxj1cf8z2a4jbzucqcivwvkoh9uaecnlgqpzwy6bmraynt9rl7mbpob449swf3nf3010o0uvweo0ty0jqshf4xzvxtmuhq5uutoyijqrra4lehasyeokf0wrdhcysxj8xyt8uc6uywmya3i8ipx9g2dha1lax1l3vzorv99qkqugxixa17pi1xua3o7z5qehlvctz6cdgef2zwleaaeyvlqn0m3hdczmgw26irn6bi0oy03k0it3hmekyxrrbmr73kokpitl1lpndke593dw5kdmp0ahjpcd191asr9ametpiks1a1rwnool8raisalbvwu0k04mjywmdwmcpn7m5nsrw505tgfv9k2708uc6syeur2f9zgqp9z35c6eu55bh4leal9ow95dpy77dtu6wu9cybq58bhdkthl0m85ekoeh8xvckpa7l6uz5vgyl0nbt3ole1hc4l4wtplgddtkulbds7egyp8nk2tf26t6kg7lunqwxm83b8m6mynhjdfxgnns8l3j2v2nku5z1auibmmc2x83013aqvor4teasklqkywhxdjjxrz2jbwwkqu6jed9gn83mxsg5ppzz9w0kschteeukmoic28wqq1pldsjlzmfptu3aod17o7gbeteenilm4pplg6yr0m0he7odgmq9pb17v9bekfllcbu8djj5e3e0uklethkcrmqr7q35avf1xpsvy5fod6ub2ra1awtoqbo26u2ydmkbotp4wuuwx3201so0gfhjs37bss3410780rqbke58loyad0xlldz4eunjezj769hm9jn1f6ne1lmrokw4l36v6w2tyf8z5f2mp2vqbhtkspnfeukopw3q3mnpk4gxsekj3wv2gl85yhu37og2qhu027fz1c4xq3jvc2q8szqi2b3rwdykfq50ii8nct0rh8apgpdin6w674khok0551tr6v1wrevoje3v823263in5atvkwn9gbcfjr3yy64ncyuo5q48rghc73uiak27e3od8ipzs2k2ojxl6a1exvdcyv3y2fu3j0wmnqbdxcwrvysyz43a1lhzm6t4mzkeciqg4j81w3q9i7vch81nc6c663r20iwek4cd3dk2qyizivbk3yfcrcsyy17p30jmwp2u1ogjpbw6ckjrzd5z8qab61vjq98hwhiua5qb8kvkp1datpqoxxh286k3mu6uhauv95nhajs5sf3j3f7xyvgz0d2omk4ro1umbqzjs5i4lyhns35sqm1u6sycfkeu2po70dgsoy5abl7csfvwjovz05pp338pnkx7dfvz952utwpiyxx261rolsm1eqc8mvmhw3e2o6adxdwdnjn1vxorfgm65rx20ztnc80nwmfcgbql87bz805xvb4lfq3lsnguvw4a13jqroa6xjhvnnb514qp9jgeytmduc95t5eqbuu3yqtps6bhn0nhsr2qmbtrjf609yx2n5a8k8hns6gox0tjq26wtn9arjsrige2is9e6v56fa62x3nynnnsbri6gbf3e2pituvua6i9z6kc4brf9f671e2zoa6t9f1ix1akwl5jp51tcadyswwot7g7125hct72h5hnctytcen6gc0qcsgl31xpb5bs5qw59v9wzu7eba6sr3trwstiioj7og6y2h69x3vy502ei1gnjchmfhl65jd02mhdinzzv55rl2w8u1uxoiofzt89lbqre1pq8kwyo28cg6296llkfpmlaak16httutriqn9bitfrh2p1vr6htuzjxiif4ss5m601kris67x04ni7g5eb6dpdiqmwb6yx0mtaj8pccww27bom5lwnxpuow6kg7e7wag7w0pfp50349pm9qdr550a9wc0dbfr2v3ezmrvbdwjvu7tu59i8odas8i29rmimjj7h3ga5ox0d50n1vwaq06c5o5pm2emokprk3xi7x25af8nayygnwvynl3863vxo6w0qke1yywr2fk42xcecymirqzfxhl967hbw89v44pschg8bw0cod5fx0s7cmi3vihlelu0b0pmselqozqz2g23285gec4zqfq86b7ut3aqr8ofi1m1f2u193fxixirtco0hhstcla8rkhgcl04mpjfefyti9ka86scfpb74stomed4maim6b329d91x1oonkkbqm9kjd6xl57v1zhesz3or8nofup3esvux980b3zwstulip20ug3hrh18pc3sgfnnjt65x697t1n22jef31s9rulfk9ad6qmd12ytyybxkikq98frkg434q4quvzvte9z6376hgt880zh0ly4gtopdc8jg3c7w534oezei8ytlj8qfliccuv1h2profbor9rbn78tp3jw5ww4xzc2rq8hg14wkss2tlr6xve62u256ohwfv8xd6i9wwn3jztv7cit60m2ui0d2xnj7k5btza5upm81efq4ymwewuzvru6qsavg1w50n0joic98sejzdo3kieunrzxm9wku7i4011z21mgfydsc4h4vfhjf73tnv3obko3irds88mwyu5yr77qy1urkvnoet03nv6oso9s7gyn0fz0t9600niaa46cf9wmp7yaj84r8s1tp35im
	=== YOUR ANSWER IS HERE ===


After learning how the library of babel works, we know we have these parameters. 

	Hex Name: <the long string of hex>
	Wall: 3
	Shelf: 5
	Volume: 25
	Page: 248


Now visit [the page](https://libraryofbabel.info/book.cgi?22syz7u9dogitfxlezobhobeuno6pnec20n6bqfg22cqihe41hbbi8aut4t618oj4wee4to32mdfmmsykl76r002hfbsurum4rr6tprxi4yinrzlqee17y5sfw11k5ybxsie6icu2x6fxvbq2wskzjtmng31ejzfikwj9ql0nxutriwr6p6vqzpdl1thkgt0o4is7znam9xub632v5mi39t8oae98kv5faatt11zitxmuka8qdrhbyw02i89fx9desufb6giwvgsvgrd18925zrgrqai31l92i6qplb9embayx8gmhqczl4gi9mb112plzs78w38hhbqmximi718hte6tw6b2m42xfwh3nnby2jemn0sz80hevqccfpyqd674swckdyaaptdp482x25uanhh5q8r0xqtokgwb8lbn41vl4mhhfvoeippvnl1t3ojshstgwumk48q8l3m937sou6b1838u7pie8da6gh8d8q5e09vazbdpsbtwyu35we0vu1r9cxfsaeisivqa01nrols0xculnijghh4goztt2ymrt2h54hfbg8o5w03ai9ghobywjxxd8erazpyjisdnrehi3xvh6yz6gnynrsgbzek9uv2poyrdld0quk3cxj1cf8z2a4jbzucqcivwvkoh9uaecnlgqpzwy6bmraynt9rl7mbpob449swf3nf3010o0uvweo0ty0jqshf4xzvxtmuhq5uutoyijqrra4lehasyeokf0wrdhcysxj8xyt8uc6uywmya3i8ipx9g2dha1lax1l3vzorv99qkqugxixa17pi1xua3o7z5qehlvctz6cdgef2zwleaaeyvlqn0m3hdczmgw26irn6bi0oy03k0it3hmekyxrrbmr73kokpitl1lpndke593dw5kdmp0ahjpcd191asr9ametpiks1a1rwnool8raisalbvwu0k04mjywmdwmcpn7m5nsrw505tgfv9k2708uc6syeur2f9zgqp9z35c6eu55bh4leal9ow95dpy77dtu6wu9cybq58bhdkthl0m85ekoeh8xvckpa7l6uz5vgyl0nbt3ole1hc4l4wtplgddtkulbds7egyp8nk2tf26t6kg7lunqwxm83b8m6mynhjdfxgnns8l3j2v2nku5z1auibmmc2x83013aqvor4teasklqkywhxdjjxrz2jbwwkqu6jed9gn83mxsg5ppzz9w0kschteeukmoic28wqq1pldsjlzmfptu3aod17o7gbeteenilm4pplg6yr0m0he7odgmq9pb17v9bekfllcbu8djj5e3e0uklethkcrmqr7q35avf1xpsvy5fod6ub2ra1awtoqbo26u2ydmkbotp4wuuwx3201so0gfhjs37bss3410780rqbke58loyad0xlldz4eunjezj769hm9jn1f6ne1lmrokw4l36v6w2tyf8z5f2mp2vqbhtkspnfeukopw3q3mnpk4gxsekj3wv2gl85yhu37og2qhu027fz1c4xq3jvc2q8szqi2b3rwdykfq50ii8nct0rh8apgpdin6w674khok0551tr6v1wrevoje3v823263in5atvkwn9gbcfjr3yy64ncyuo5q48rghc73uiak27e3od8ipzs2k2ojxl6a1exvdcyv3y2fu3j0wmnqbdxcwrvysyz43a1lhzm6t4mzkeciqg4j81w3q9i7vch81nc6c663r20iwek4cd3dk2qyizivbk3yfcrcsyy17p30jmwp2u1ogjpbw6ckjrzd5z8qab61vjq98hwhiua5qb8kvkp1datpqoxxh286k3mu6uhauv95nhajs5sf3j3f7xyvgz0d2omk4ro1umbqzjs5i4lyhns35sqm1u6sycfkeu2po70dgsoy5abl7csfvwjovz05pp338pnkx7dfvz952utwpiyxx261rolsm1eqc8mvmhw3e2o6adxdwdnjn1vxorfgm65rx20ztnc80nwmfcgbql87bz805xvb4lfq3lsnguvw4a13jqroa6xjhvnnb514qp9jgeytmduc95t5eqbuu3yqtps6bhn0nhsr2qmbtrjf609yx2n5a8k8hns6gox0tjq26wtn9arjsrige2is9e6v56fa62x3nynnnsbri6gbf3e2pituvua6i9z6kc4brf9f671e2zoa6t9f1ix1akwl5jp51tcadyswwot7g7125hct72h5hnctytcen6gc0qcsgl31xpb5bs5qw59v9wzu7eba6sr3trwstiioj7og6y2h69x3vy502ei1gnjchmfhl65jd02mhdinzzv55rl2w8u1uxoiofzt89lbqre1pq8kwyo28cg6296llkfpmlaak16httutriqn9bitfrh2p1vr6htuzjxiif4ss5m601kris67x04ni7g5eb6dpdiqmwb6yx0mtaj8pccww27bom5lwnxpuow6kg7e7wag7w0pfp50349pm9qdr550a9wc0dbfr2v3ezmrvbdwjvu7tu59i8odas8i29rmimjj7h3ga5ox0d50n1vwaq06c5o5pm2emokprk3xi7x25af8nayygnwvynl3863vxo6w0qke1yywr2fk42xcecymirqzfxhl967hbw89v44pschg8bw0cod5fx0s7cmi3vihlelu0b0pmselqozqz2g23285gec4zqfq86b7ut3aqr8ofi1m1f2u193fxixirtco0hhstcla8rkhgcl04mpjfefyti9ka86scfpb74stomed4maim6b329d91x1oonkkbqm9kjd6xl57v1zhesz3or8nofup3esvux980b3zwstulip20ug3hrh18pc3sgfnnjt65x697t1n22jef31s9rulfk9ad6qmd12ytyybxkikq98frkg434q4quvzvte9z6376hgt880zh0ly4gtopdc8jg3c7w534oezei8ytlj8qfliccuv1h2profbor9rbn78tp3jw5ww4xzc2rq8hg14wkss2tlr6xve62u256ohwfv8xd6i9wwn3jztv7cit60m2ui0d2xnj7k5btza5upm81efq4ymwewuzvru6qsavg1w50n0joic98sejzdo3kieunrzxm9wku7i4011z21mgfydsc4h4vfhjf73tnv3obko3irds88mwyu5yr77qy1urkvnoet03nv6oso9s7gyn0fz0t9600niaa46cf9wmp7yaj84r8s1tp35im-w3-s5-v25:248) and we see the text

	congrats, your key is averyunobviouskey.                                        


## Flag

	averyunobviouskey