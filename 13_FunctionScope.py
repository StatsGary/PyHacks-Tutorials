# =============================================================================
# Title             PyHacks - Classes  - Scope
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

#-----------------------LOCAL SCOPE----------------------------------------

def print_name(name):
    name = str(name)
    print("The name inputted is {}".format(name))
    
print_name("Gary Hutson")

# Function factory - function factory
# Local scope works here, as the inner function is outside of the 
# outer function i.e. inner_function() is contained inside scope_message()

def scope_message():
    scope_message = "I am local"
    def inner_function():
        print("*" * 75)
        print(scope_message)
    inner_function()
    
scope_message()

#-----------------------GLOBAL SCOPE----------------------------------------

# A variable created outside of a function can be used by anyone
scope_message = "I am global baby!"

def print_message():
    print(scope_message)
    
# Call function
print_message()

# Same variable name
scope_message = "Still global"

def print_message():
    scope_message = "Are you local"
    print("*" * 75)
    print (scope_message)
    
print_message() #This will get the local print by calling the function
# The scope message is above the def argument
print(scope_message)


# Want to make a variable global inside a function. The global command to the rescue
scope_msg = "I am available globally!"
def scope_msg():
    #This is the magic sauce
    global scope_msg
    scope_msg = "I should be local, but the global keywords has made me global!"
    print("*" * 75)
    
scope_msg()
print(scope_msg)
