# =============================================================================
# Title             PyHacks - namedtuples
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      23/05/2022
# =============================================================================

from collections import namedtuple

rockers_list = [
    ('Dave Grohl', ' Foo Fighters'),
    ('Jimmy Page', 'Led Zeppelin'),
    ('Robert Plant', 'Led Zeppelin'),
    ('Roger Daltrey', 'The Who'),
    ('James Hetfield', 'Metallica'),
    ('Dave Mustaine', 'Megadeth'),
    ('Eddie Vedder', 'Pearl Jam'),
    ('Ronnie James Dio', 'Dio'),
    ('Howard Jones','Killswitch Engage')
]

# To get the names in a loop the standard way
for rocker in rockers_list:
    print('The rockers name is {}'.format(rocker[0]))

# Here to get the name we would need to get the zero index, as the name is stored in the zero index
# Here comes the power of the named tuple
Rockers = namedtuple('Rockers', ['rocker_name', 'band'])
rocker_named_tuple_list = [
    Rockers('Dave Grohl', ' Foo Fighters'),
    Rockers('Jimmy Page', 'Led Zeppelin'),
    Rockers('Robert Plant', 'Led Zeppelin'),
    Rockers('Roger Daltrey', 'The Who'),
    Rockers('James Hetfield', 'Metallica'),
    Rockers('Dave Mustaine', 'Megadeth'),
    Rockers('Eddie Vedder', 'Pearl Jam'),
    Rockers('Ronnie James Dio', 'Dio'),
    Rockers('Howard Jones','Killswitch Engage')
]

# Now we should be able to replicate the above example, but without having to specify an index, instead we can use
# a name

for rocker in rocker_named_tuple_list:
    print(f'Rocker is: {rocker.rocker_name} and band is: {rocker.band}')


# Change value in named tupled 
replace_example = rocker_named_tuple_list[0] # Get Dave Grohl and add his band to Nirvana
replace_example = replace_example._replace(band='Nirvana')
print(replace_example)


# Convert a dictionary into a named tuple
my_rocker_dict = {'rocker_name': 'Zack De La Rocha', 'band':'Rage Against The Machine'}
make_dict_named_tuple = Rockers(**my_rocker_dict)
print(make_dict_named_tuple)

# Make a list into a namedtuple automatically
rocker_list_make = ['Kurt Cobain', 'Nirvana']
rocker_made_from_list = Rockers._make(rocker_list_make)
print(rocker_made_from_list)
