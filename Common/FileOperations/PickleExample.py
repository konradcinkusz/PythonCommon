# HOW TO USE PICKLE, HOW TO APPEND TO EXISTING FILE WITH PICKLE DUMP

#%% https://stackoverflow.com/a/55474324/4510954
import pickle
import numpy as np

PATH = r'PATH TO MY SET'
a = np.arange(-100,100)
test = list(np.random.choice(list(np.select([a != 0, a == 0], [a, -1])), 100))
interval = 10
counter = 0

trainResult = []
with open('trainset', 'ab') as file :
    _ = [pickle.dump(i, file) for i in trainResult]

for i in test :
    with open(PATH + '\\' + 'trainset', 'ab') as file :
        pickle.dump(i, file)
    #trainResult.append(i)
    #if counter % interval == 0 :
    #    with open(PATH + '\\' + 'trainset', 'ab') as file :
    #        pickle.dump(trainResult, file)
    #        trainResult = []

with open(PATH + '\\' + 'trainset', 'rb') as file :
    arrTMP = [pickle.load(file) for i in range(len(test) - 1)]

print(arrTMP)

#%% https://stackoverflow.com/a/28078606/4510954
import pickle as dill

scores = [('joe', 1), ('bill', 2), ('betty', 100)]
nscores = len(scores)

print(scores)

with open('high', 'ab') as f:
    _ = [dill.dump(score, f) for score in scores]


with open(PATH + '\\' + 'high', 'ab') as f:
    dill.dump(('mary', 1000), f)

# we added a score on the fly, so load nscores+1
with open(PATH + '\\' + 'high', 'rb') as f:
    _scores = [dill.load(f) for i in range(nscores + 1)]

print(_scores)
#[('joe', 1), ('bill', 2), ('betty', 100), ('mary', 1000)]

