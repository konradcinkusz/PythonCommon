#%%
dictionary = { "key" : "value", "key1" : "value", 2123 : 4554, "other_key" : "other_value" }

#%%
#Get dictionary keys
dictionary.keys()

#%%
#list of dictionary keys, list(..) construct new list
list(dictionary.keys())
#list of dictionary values
list(dictionary.values())

#%%
dictionary_keys = list(dictionary.keys())
print (dictionary_keys is list(dictionary.keys()))
#hard copy of dictionary keys
hard_copy = dictionary_keys
print(hard_copy is dictionary_keys)
hard_copy = dictionary_keys[:]
print(hard_copy is dictionary_keys)
print (hard_copy is list(dictionary.keys()))

#%%
#does not work:
#dictionary.has_key('klucz')
#instead of
'key' in dictionary
'key' in dictionary.keys()
'value' in dictionary.values()
try :
    try :
        print(dictionary['value'])
    except KeyError as ke :
        print('Value key does not exist')
    #Add value 'bacon' with new key named 'value'
    dictionary['value'] = 'bacon'
    print(dictionary['value'])
    del dictionary['value']
    try :
        print(dictionary['value'])
    except KeyError as ke :
        print('Value does not exist - again')

except Exception as ex :
    print('differen exception', ex)

#%% Dictionaries sorting
#does not work because different key type
for sortedKey in list(dictionary.keys()).sort() : #sort is nonetype
    print(str(dictionary[sortedKey]))

#%% Sorting dictionary
dictionary = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'g' : 6, 'l' : 7}
print(dictionary)
print(sorted(dictionary))
keys = list(dictionary.keys())
keys.sort()
for sortedKey in keys :
    print(dictionary[sortedKey]) 
dictionary = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'g' : 6, 'l' : 7}
for sortedKey in sorted(list(dictionary.keys())) :
    print(dictionary[sortedKey]) 
    

#%% https://stackoverflow.com/a/613218/4510954
import collections
sorted_dict = collections.OrderedDict(dictionary)
