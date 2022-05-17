# =============================================================================
# Title             PyHacks - Dealing with multiple arguments
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      16/05/2022
# =============================================================================

def test_mult_arguments(norm_arg, *args_values):
    print(f'First argument is {norm_arg}')
    # Iterated through additional arguments and print
    for arg in args_values:
        print('Passed another argument (*arg_values):', arg)

# Let's test our function to capture original passed argument and additional arguments

test_mult_arguments('this is my normal argument', 'additional argument 1', 'additional argument 2',
                    'additional argument 3')



# Second example - create sum function to work with arguments
def summer_function(*range):
    result = 0
    print(type(range)) # Check how the args are stored
    for val in range:
        result += val
    return result

# Use the new function
print(summer_function(20,40,60,80,100))


# Work with kwargs

def working_with_kwargs(**my_k_wargs):

    for key, value in my_k_wargs.items():
        print('{0}={1}'.format(key, value))
        if key == 'fav_food':
            print(f'Item contains his favourite food {value}.')

        if key == 'first_name':
            print(f'His name is {value}')

        


result = working_with_kwargs(first_name='Gary', occupation='ML Engineer Lead', 
                    fav_food='Fish')





# Ordering of arguments in function
def argument_ordering(x,y, *args, **kwargs):
    print('Normal arguments: ',x,y)
    for arg in args:
        print (arg)

    for key, value in kwargs.items():
        print(key, value)



argument_ordering(x=1, y=2, args=(1,2,3,5), is_a_kwarg='Yes')



# Unpacking arguments
def sum_unpacking(x1,x2,x3):
    print(x1 + x2 + x3)

list_of_vals = [20,40,20]
sum_unpacking(*list_of_vals)

# Unpacking with args and kwargs

#Merging lists with unpacking and args

list1 = [(x + 1) ** 3 for x in range(10)]
list2 = [(x + 3) ** 3 for x in range(10)]
list3 = [(x + 10) ** 3 for x in range(10)]

list_of_lists = [*list1, *list2, *list3]
print(len(list_of_lists))
print(list_of_lists)

# Merging dicts with kwargs 
dict1 = {'x1': 10, 'x2': 30}
dict2 = {'x3': 20, 'x4': 32}
merge_the_dicts = {**dict1, **dict2}
print(merge_the_dicts)