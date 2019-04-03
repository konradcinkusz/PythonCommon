#%%
def adder(*varargs) :
    sum = varargs[0]
    for i in range(1,len(varargs)):
        sum += varargs[i]
    return sum

A = [1,3,4,5]
B = [4,6]
C = [5,6,8]
#If I call this script from local python interactive (no to anaconda) the result should be packed in print function
adder(A,B,C)

A_dict = {'class' : 'Andy', 'home' : 'California'}
B_dict = {'Name' : 'Lucy', 'home' : 'Estonia'}
C_dict = {'surname' : 'Smith'}
adder(A_dict,B_dict,C_dict) # to już dodać po swojemu

