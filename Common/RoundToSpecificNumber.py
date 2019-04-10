#%% Round to specific fraction

def round(num, x, y) :
    av = (x+y)/2
    if num % 1 < av :
        return int(num)+x
    return int(num)+y

import builtins
def round(number):
    x=0.5
    y=0.9
    if type(number) is float: 
        av = (x+y)/2
        if number % 1 < av :
            return int(number)+x
        return int(number)+y
    return None
