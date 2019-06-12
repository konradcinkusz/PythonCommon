#%% https://stackoverflow.com/a/176921/4510954
[1, 1].index(1)
[i for i, e in enumerate([1, 2, 1]) if e == 1]
g = (i for i, e in enumerate([1, 2, 1]) if e == 1)
next(g)
next(g)

#%%
def indexer(word, words) :
    #return array of indexes of word in words list if exist, else return empty array
    #return [i for i,e in enumerate(words) if sentence in e]
    return [i for i,e in enumerate(words) if e == sentence]


#%%
