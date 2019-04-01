#%% EXAMPLE CODE FROM PYTHON INTRODUCTION 2002 CHAPTER 3 EX 4
L = [1,2,4,8,16,32,64]
X = 5

found = i = 0
#check if 2^5 are on list
while not found and i < len(L) : 
    if 2 ** X == L[i] :
        found = 1
    else :
        i += 1

if found :
    print ('na pozycji: ', i)
else :
    print (2**X, 'nie znaleziono')

#%% pozbycie się znacznika found za pomocą else
while i < len(L) :
    if 2 ** X == L[i] :
        print('znaleziono na pozycji: ', i)
        break
else :
    print (2**X, 'nie znaleziono')

#%% for else w celu pozbycia się jawnego indeksowania
for i in L:
    if 2**X == i :
        print('znaleziono na pozycji: ', L.index(i))
        break
else :
    print (2**X, 'nie znaleziono')

#%% usuwamy pętle dodajemy operator in
if 2**X in L :
    print('znaleziono na pozycji: ', L.index(2**X))
else :
    print (2**X, 'nie znaleziono')

#%% for and append to generate 2^X
L = []
for i in range(0,100) :
    L.append(2**i)
print(L)

#%% map to generate 2^X
L = map(lambda x : 2**x, range(0,100))
print(list(L))

