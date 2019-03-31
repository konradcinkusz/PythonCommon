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
