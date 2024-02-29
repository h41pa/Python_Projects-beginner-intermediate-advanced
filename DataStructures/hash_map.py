
# Creating a hash map (dictionary)
my_dict = {}


# Adding key-value pairs

my_dict['Maria'] = 8
my_dict['Mihai'] = 7
my_dict['Andrei'] = 10

# Accessing values using keys
print(f'Maria grade for test: {my_dict["Maria"]}')

# Checking if a key exists

if 'Mihai' in my_dict:
    print(f'Maria grade for test: {my_dict["Mihai"]}')

# Updating a value
my_dict['Mihai'] = 9

# Deleting a key-value pair

del my_dict['Maria']

# Iterating through keys and values

for key, value in my_dict.items():
    print(f'{key} - {value}')
