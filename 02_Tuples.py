# =============================================================================
# Title             PyHacks - Tremendous Tuples
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      01/07/2021
# =============================================================================

# ------------- Creating your first tuple------------------#

euro_2020_winners = ("England", "Switzerland",
                     "Spain", "Belgium", "Italy", "Ukraine",
                     "Czech Republic", "Denmark")
print(euro_2020_winners)
print(type(euro_2020_winners))

# ------------- Access Tuple Items -------------------------#

print(euro_2020_winners[0])
# Negative to get the last team
print(euro_2020_winners[-1])
#Range of indexes
print(euro_2020_winners[0:3])
#Using the colon
print(euro_2020_winners[2:])
# Range of negative indexes
print(euro_2020_winners[-3:-1])
# Checking if item exists
if "England" in euro_2020_winners:
    print("Yes this item is in the remaining stages of Euro 2020")
    
# ------------- Update Tuples -------------------------#
# =============================================================================
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# =============================================================================

# Hack
copy_euro = euro_2020_winners
copy_euro = list(copy_euro)
copy_euro[7] = "Sweden"
copy_euro = tuple(copy_euro)
print(copy_euro)

# Hack for appending
del copy_euro
euro_append = euro_2020_winners
euro_append = list(euro_append)
euro_append.append("Germany")
euro_append = tuple(euro_append)

# Hack for adding tuples
del euro_append
euro_add = euro_2020_winners
new_value = ("Germany",) #One element tuples need a comma afterwards
euro_add += new_value
print(euro_add)


# ------------- Unpacking Tuples -------------------------#

# When tuples are created we assign values, or pack them

(team1, team2, team3, team4, team5, team6, team7, team8) = euro_2020_winners
print(team1)

# ------------- Looping a tuple  -------------------------#

for i, team in enumerate(euro_2020_winners):
    print("The Euro 2020 team is {}. At tuple index {}.".format(team, i))

# Doing this with a while loop 
i = 0
while i < len(euro_2020_winners):
    print(euro_2020_winners[i])
    i = i + 1
    
# ------------- Joining a Tuple  -------------------------#
joined = euro_2020_winners + euro_add
print(joined)
