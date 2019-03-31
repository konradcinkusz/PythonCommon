#%%
example_string = "Lorem impsum"
#sum of ASCII values of example_string
sum = 0
example_string_ASCII_values = []
for e in example_string :
    print(ord(e))
    sum += ord(e)
    example_string_ASCII_values.append(ord(e))

print('Sum of example string ASCII values', sum)

#Use map to do same thing:
example_string_ASCII_values_map = list(map(ord, example_string))
print(example_string_ASCII_values == example_string_ASCII_values_map)

#%%
for i in range(500000) :
    print('hello %d\n\a' % i)

