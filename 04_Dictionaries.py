# =============================================================================
# Title             PyHacks - Dictionaries
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      06/07/2021
# =============================================================================

# ------------- Creating your first dictionary------------------#

# Premised on  a dataset package I co-created with some fellow R chums
# https://cran.r-project.org/web/packages/NHSRdatasets/vignettes/stranded_model.html

dict_ae = {
    "stranded_patient_ID": [1, 2],
    "patient_age": [23, 24],
    "care_home_ref_flag": [1,0],
    "pat_surname": ["Smith", "Hutson"]
    }

print(dict_ae)
# Get the type
print(type(dict_ae))


# ------------- Access Dictionary Items ------------------#

# By name
pat_id = dict_ae.get("stranded_patient_ID")
print(pat_id)

# By keys
dict_keys = dict_ae.keys()
print(dict_keys)

# ------------- Change Dictionary Items ------------------#

dict_ae["patient_age"][0] = 24
print(dict_ae)

# Using the update method
dict_ae.update({"care_home_ref_flag": [1,1]})
print(dict_ae)

# ------------- Adding Dictionary Items ------------------#

dict_ae["frail"] = ["Yes", "No"]
print(dict_ae)

# Update dictionary

dict_ae.update({"frail": ["No", "Yes"]})

# ------------- Removing Dictionary Items ------------------#
ae_copy = dict_ae.copy()

# Remove column
ae_copy.pop("patient_age")
# Use popitem
ae_copy.popitem()
print(ae_copy) # This deletes the last item in the dictionary
# Using the del keyword
del ae_copy["pat_surname"]
# Clearing the values in the dictionary
ae_copy.clear()
print(ae_copy)
# Deleting the dictionary from memory
del ae_copy

# ------------- Looping through dictionaries-----------------#
# Get columns
for dict_i in dict_ae:
    print("[COLUMN] The current column is: {}".format(dict_i))
    
# Print all values one by one

for dict_i in dict_ae.values():
    print(dict_i)
    
# Use the keys method to return the keys
for dict_i in dict_ae.keys():
    print(dict_i)    
    
# Ideally, we would want keys and values in one 
empty_list = []
for key, item in dict_ae.items():
    print("The key is: {} and the item(s): {}".format(key, item))
    empty_list.append([key, item])
    print("Added dictionary items to a list")

    
# ------------- Copying dictionaries -----------------#

# Method one
copy_one = dict_ae.copy()
# Method two
copy_two = dict(dict_ae)

# ------------- Nested dictionaries   -----------------#

# Create a dictionary that has three dictionaries nested inside

patients = {
    "patient1": {
        "name": "Gary Hutson",
        "admission_date": "2017-01-03"},
    "patient2": {
        "name": "Trevor Hutson",
        "admission_date": "2018-03-12"} }

# Or

pat1 = {"name": "Gary Hutson", "admission_date": "2018-03-12"}
pat2 = {"name": "Trevor Hutson", "admission_date": "2019-01-23"}
patients2 = {"patient1":pat1,
             "patient2":pat2}

print(patients2)
