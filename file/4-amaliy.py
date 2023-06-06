# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 02:37:19 2023

@author: User
"""

def ar_pr_sum(a1, d, N):
    if N == 1:
        return a1
    else:
        return a1 + ar_pr_sum(a1 + d, d, N - 1)
a1 = 2
b1 = 4
c1 = 6
d1 = 3
d2 = 2
d3 = 4
N = 5
M = 3
K = 4

result = ar_pr_sum(a1, d1, N) + ar_pr_sum(b1, d2, M) + ar_pr_sum(c1, d3, K)
print("Yig'indisi:", result)
