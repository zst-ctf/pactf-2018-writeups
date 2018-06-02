#!/usr/bin/env python3
import string

text = 'ny_nx_tsq3_zumnqq_kwtr_mjwj_68aad68ba8'
charset = 'abcdefghijklmnopqrstuvwxyz0123456789'

def emperor(s):
    # lowercase letters and spaces
    rotated = charset[1:] + charset[0]
    return s.translate(str.maketrans(rotated, charset))

for i in range(len(charset)):
    text = emperor(text)
    print(i, text)
