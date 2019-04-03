#%% Python introduction function chapter
X = 99
def selector() :
    print(X) # call global variable

#%% Exception because python compilator thinks that X is not a global but local uninitialized
X = 99
def selector() :
    print(X) # call global variable
    X = 8 

#%% To use global 
X = 99
def selector() :
    global X
    print(X) # call global variable
    X = 8 # works but it also change global now

#%% If i would like truly use global variable than init local and set value of local variable
X = 99
def selector() :
    import __main__ #import outer module
    print(__main__.X) #__main__ -> global names classification
    X = 88 #not classified local
    print (X) #use local


