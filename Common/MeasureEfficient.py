import time
from time import perf_counter as pc

t0=pc()    
a = set(y_pred).intersection(y_test)
f = [1 if i in a else 0 for i, j in enumerate(y_pred)]
t1 = pc() - t0

t0=pc()
for i in range(len(y_pred)):
    mask = (y_pred[i] == y_test[i]) * 1
    masks_list.append(mask)
t2 = pc() - t0

val = t1 - t2
