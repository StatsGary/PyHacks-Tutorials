# =============================================================================
# Title             PyHacks - defaultdict
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      23/05/2022
# =============================================================================


from collections import defaultdict
# Example 1
# Function to return a default value if it fails
def default_val():
  return 'This key was not found in the dictionary'

# Define the dictionary
dd = defaultdict(default_val)
# Add values to the dictionary
dd['key1'] = 100
dd['key2'] = 200

# Print out the dictionary
print(dd['key1'])
print(dd['key2'])
print(dd['key3'])

# Example 2 - __missing__
dd = defaultdict(lambda: 'Key not present in this dictionary')
dd['key1'] = 'Gary'
dd['key2'] = 'Charlie'

# Provide the default value for the key
print(dd.__missing__('key3'))
print(dd.__missing__('key4'))

# Example 3 - using int with the default_factory argument of defaultdict
dd = defaultdict(int)
list_dd = [1,2,3,4,2,4,1,2]

# Iterate through the list
for idx in list_dd:
    dd[idx] +=1

print(dd)
