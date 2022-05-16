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
        print('Arguments passed:\n', '-'*80)
        print('{0}={1}'.format(key, value))

        if key == 'fav_food':
            print(f'Item contains his favourite food {value}.')

        if key == 'first_name':
            print(f'His name is {value}')



working_with_kwargs(first_name='Gary', occupation='ML Engineer Lead', 
                    fav_food='Fish')