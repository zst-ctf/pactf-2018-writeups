# Straight From The Emperor
10 points

## Challenge 
> The Emperor says `ny_nx_tsq3_zumnqq_kwtr_mjwj_68aad68ba8`–what could it possibly mean? I hear that he ‘encrypts’ numbers now too, something about appending them to the alphabet…



## Hint
> Some say he’s an emperor, I say he’s a salad.



## Solution

#### Analysis:
 - `something about appending them to the alphabet`: means that ceasar cipher but with numbers
 - `he’s a salad`: means caesar cipher

#### Solving 

The custom caesar cipher charset is `abcdefghijklmnopqrstuvwxyz0123456789`

Create a script to rotate about the charset...

	$ python3 solve.py 
	0 mx_mw_srp2_ytlmpp_jvsq_livi_5799c57a97
	1 lw_lv_rqo1_xskloo_iurp_khuh_4688b46986
	2 kv_ku_qpn0_wrjknn_htqo_jgtg_3577a35875
	3 ju_jt_pomz_vqijmm_gspn_ifsf_2466924764
	4 it_is_only_uphill_from_here_1355813653
	5 hs_hr_nmkx_toghkk_eqnl_gdqd_0244702542
	6 gr_gq_mljw_snfgjj_dpmk_fcpc_z1336z1431
	...

We see a legible string after 4 rotations


## Flag

	it_is_only_uphill_from_here_1355813653