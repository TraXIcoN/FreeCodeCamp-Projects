
"""Regex substitution problem"""

"""You are given a text of lines. The text contains && and || symbols.
Replace &&--and , ||--or"""
        

#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

import re
n=int(input())
for i in range(n):
    a=input()
    val=re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x :'and' if x.group()=='&&' else 'or',a)
    print(val)