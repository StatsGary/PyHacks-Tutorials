# =============================================================================
# Title             PyHacks - Sets
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      06/07/2021
# =============================================================================

# ------------- Creating your first set object ------------------#

# A set is unordered and unindexed and is used to store multiple items in
# a single variable
# Due to the fact that sets are unordered, you cannot be sure in which order they 
# will appear

films = {"Jurassic Park", "Shawshank Redemption", "Green Mile"}

# Try and add a duplicate
films = {"Jurassic Park", "Shawshank Redemption", "Green Mile", "Green Mile"}
# Notice the additional Green Mile is not added

# ------------- Accessing set items -----------------------------#

for set_i in films:
    print("The current movie / film is: {}".format(set_i))
    
# Check if item exists in set
print("Jurassic Park" in films)

# ------------- Changing items ----------------------------------#
# Once a set is created, you cannot change its items. 

# ------------- Add set items -----------------------------------#
films.add("Eurovision: Fire Saga")
print(films)

# Add items from another set
horror_films = {"The Shinning", "Dusk Til Dawn"}
films.update(horror_films)
print(films)

# The object in the update method does not need to be a set item
thrillers = ["The Bone Collector", "The Girl With The Dragon Tattoo"]
films.update(thrillers)

# ------------- Removing set items--------------------------------#
films_orig = films.copy()
# Remove method
films.remove("Jurassic Park")
print(films)
# Discard method
films.discard("The Bone Collector")
print(films)
# Remove last item with pop method
films.pop()
print(films)
# Clear the set
films.clear()
print(films)
# Delete the entire set from memory
del films

# ------------- Looping through sets -----------------------------#

for set_i in films_orig:
    print(set_i)
    
    
# ------------- Joining sets ------------------------------------#
film_index = {1,2}
thrillers_with_index = horror_films.union(film_index)


# Keeping only duplicates
film1 = {"Jurassic Park", "Scream", "Forrest Gump"}
film2 = {"Scream", "Shawshank Redemption"}

# Create copies
f1_copy = film1.copy()
f2_copy = film2.copy()


film1.intersection_update(film2)
print(film1)

# Keep all but not the duplicates
f1_copy.symmetric_difference_update(f2_copy)
print(f1_copy)

# To return a new set of each of the above, use the intersection and symmetric_difference commands
# as the update function will change the original values

# ------------- Logical Operators----------------------------------#
film1 = {"Jurassic Park", "Scream", "Forrest Gump"}
film2 = {"Scream", "Shawshank Redemption"}

# The isdisjoint() method returns True if none of the items are present in both sets, 
# otherwise it returns False.
disjoint = film1.isdisjoint(film2)
print(disjoint)

# issubset method
# This method returns True if all the items in the set exist in a comparison set
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
is_sub = film1.issubset(film2)
print(is_sub)

# issuperset
is_super_set = film1.issuperset(film2)
print(is_super_set)
is_super = film1.issuperset(film1)
print(is_super)


