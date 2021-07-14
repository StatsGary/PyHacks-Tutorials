# =============================================================================
# Title             PyHacks - File Input and Output
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      14/07/2021
# =============================================================================

# FILE HANDLING codes
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# HANDLING MODE
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#---------------------------READ FILE----------------------------------------

# Opening a file and reading it
path = "Data/Stranded/stranded.txt"
file = open(path, "r")
print(file.read())

# Read the first 10 characters of a file
file_part = open(path, "r")
print(file_part.read(10))

#---------------------------WRITE FILE----------------------------------------
# # Append content to existing file
path2 = "Data/Stranded/stranded_added.txt"
file = open(path2, "a")
file.write('"769" "Stranded" 65 0 0 1 0 NA "18/01/2021" "JUST APPENDED"')
file.close()

#Clear the contents of a file
path3 = "Data/Stranded/stranded_cleared"
file3 = open(path3, "w")
file3.write("Woops - I just purged your file")
file3.close()

#---------------------------CREATE A FILE--------------------------------------
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist

file_path = "Data/Stranded/"
create_f = open(file_path + "new_file.txt", "x")
# Using the write (w) method
create_w = open(file_path + "new_file2.txt", "w")

#---------------------------DELETE FILES---------------------------------------
import os
os.remove(file_path + "new_file.txt")

# Check if a file in directory exists
concat_path = os.path.join(file_path, "new_file.txt")
if os.path.exists(concat_path):
    os.remove(file_path)
else:
    print("The file does not exist")
    
#---------------------------CREATE and REMOVE FOLDER---------------------------
# Make directory
os.mkdir(file_path + "FolderToDelete")
# Remove directory
os.rmdir(os.path.join(file_path, "FolderToDelete")) 

#---------------------------LIST DIR STRUCTURE---------------------------------
print(os.listdir(file_path))

file_to_find = "stranded.txt"
for file in os.listdir(file_path):
    if file == file_to_find:
        print("{} found!".format(file_to_find))
        found_file = open(file_path + file, "r")
        
#------------------------- WORKING WITH THE ENVIRON --------------------------
print(os.environ['USERNAME']) # Get username
#Get everything 
print(os.environ)
#Get PC name

# Cool application to shut down PC

if os.environ["USERNAME"] != os.environ["USERNAME"]:
    os.system("shutdown /s /t 1")
else:
    print("Welcome {}. How are you?".format(os.environ["USERNAME"]))
# This will never work, as your username will always not be equal
# but if you changed != to == then it would work everytime.


print(os.getcwd())



