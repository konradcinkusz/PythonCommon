#%%
L = [[0.9, 0.7] ,[0.5, 0.6], [1.1, 1.2]]
b = []
for i in range(len(L)) :
    a=1 
    for j in range(len(L[0])):
        a*=L[i][j]
    b.append(a)

#%% https://stackoverflow.com/a/55488082/4510954
from functools import reduce
from operator import mul

L = [[0.9, 0.7], [0.5, 0.6], [1.1, 1.2]]

res = sum(reduce(mul, p, 1) for p in zip(*L))
# 0.999
# version without import
s = 0
for items in zip(*L):
    prod = 1
    for factor in items:
        prod *= factor
    s += prod
