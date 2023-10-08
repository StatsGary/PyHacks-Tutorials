# =============================================================================
# Title             PyHacks - dictionary to add values
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      16/09/2022
# =============================================================================


# Assign auto key to dictionary with value
dicts = {}
values = ["Kerry", "Gary", "Charlie", "Carol"]
keys = range(len(values))

for i in keys:
    dicts[i] = values[i]

print(dicts)

# Approach to add key and value in loop

dicts = {}
keys = [10,11,12,13,14]
values = ['Gary', 'Kerry', 'Charlie', 'Carol', 'Craig']

for idx, i in enumerate(range(len(keys))):
    dicts[keys[idx]] = values[i]

print(dicts)

# Appending values

existing_dict = {
    0: 'Kerry',
    1: 'Charlie'
}

new_keys = [2,3]
values = ['Pat', 'Carol']

for i in range(len(new_keys)):
    existing_dict[new_keys[i]] = values[i]

print(existing_dict)
print(existing_dict[2])
