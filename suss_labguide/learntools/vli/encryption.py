from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import yaml
import os

def load_config(config_file='.config.yml'):
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

# Encrypt a file and save encrypted data                    
# def encrypt(self, file_path):
#     # e.g. ./suss encrypt ICT133/ict133/lab1/q1/hint
    
#     # Get encrypt option to check if allowed to encrypt
#     can_encrypt = self.find('encrypt')
    
#     if(can_encrypt):
#         # Get Encrypt Key from config
#         key = self.find('encrypt_key')
        
#         # Create a Fernet cipher instance with the key
#         cipher = Fernet(key)
        
#         # Read the file
#         with open(file_path, 'rb') as file:
#             plaintext = file.read()
            
#         # Retrieve Marker
#         marker = self.find('encrypt_marker').encode()
        
#         # Check if file is not empty first
#         if not self.is_text_empty(plaintext.decode()):
#             try:
#                 # Encrypt the plaintext
#                 encrypted = cipher.encrypt(plaintext)

#                 # Save the encrypted data to a file
#                 with open(file_path, 'wb') as file:
#                     # Concat marker with encrypted data
#                     file.write(marker+encrypted)
                    
#             except InvalidToken:
#                 print("Invalid token. Please check the encryption key or the file content.")
#         else:
#             print("Unable to encrypt as the file is empty.")
#     else:
#         print("Encrypt/Decrypt option is not enabled")

# # Decrypt a file and save decrypted string
# def decrypt(self, file_path):
#     print("did it reach here: decrypt")
#     # e.g. ./suss decrypt ICT133/ict133/lab1/q1/hint
    
#     # Get encrypt option to check if allowed to encrypt
#     can_encrypt = self.find('encrypt')
    
#     if(can_encrypt):          
#         # Get Encrypt Key from config
#         key = self.find('encrypt_key')
        
#         # Create a Fernet cipher instance with the key
#         cipher = Fernet(key)
        
#         # Read the file
#         with open(file_path, 'rb') as file:
#             encrypted = file.read()
#             print("--encrypted--")
#             print(encrypted)
        
#         marker = self.find('encrypt_marker').encode()
        
#         if(encrypted.startswith(marker)):
#             try:
#                 # Cut the marker from file content
#                 encrypted = encrypted[len(marker):]
                
#                 # Decrypt the encrypted data, then decode bytes into string
#                 decrypted = cipher.decrypt(encrypted).decode()
                
#                 # Save the decrypted string to a file
#                 with open(file_path, 'w') as file:
#                     file.write(decrypted)
                    
#             except InvalidToken:
#                 print("Invalid token. Please check the encryption key or if the file has been encrypted before.")
#         else:
#             print("This file has not been encrypted.")
#     else:
#         print("Encrypt/Decrypt option is not enabled")


def decrypt(encrypted):
    # print("did it reach here: decrypt")
    # e.g. ./suss decrypt ICT133/ict133/lab1/q1/hint
    
    # Get encrypt option to check if allowed to encrypt
    can_encrypt = find('encrypt')
    # print("did it reach here: decrypt 1")

    if(can_encrypt):          
        # Get Encrypt Key from config
        key = find('encrypt_key')
        # print("did it reach here: decrypt 2")

        
        # Create a Fernet cipher instance with the key
        cipher = Fernet(key)
        
        # print("did it reach here: decrypt 3")

        # Read the file
        # with open(file_path, 'rb') as file:
        #     encrypted = file.read()
        #     print("--encrypted--")
        #     print(encrypted)
        
        marker = find('encrypt_marker').encode()
        # print(marker)
        # print("did it reach here: decrypt 4")
        # print(encrypted)
        # print("did it reach here: decrypt 40")

        if(encrypted.startswith(marker.decode("utf-8"))):
            try:
                # print("did it reach here: decrypt 4a")
                # Cut the marker from file content
                encrypted = encrypted[len(marker):]
                # print("did it reach here: decrypt 5")
                # Decrypt the encrypted data, then decode bytes into string
                return cipher.decrypt(encrypted).decode()
                
                # Save the decrypted string to a file
                # with open(file_path, 'w') as file:
                #     file.write(decrypted)
                    
            except InvalidToken:
                print("Invalid token. Please check the encryption key or if the file has been encrypted before.")
        else:
            print("This file has not been encrypted.")
    else:
        # return the original string if encryption is not enabled
        return encrypted
        print("Encrypt/Decrypt option is not enabled")

# Find value based on a given key
def find(target_key, data=None):
    if data is None:
        data = load_config() #config_data
    
    try:
        for key, value in data.items():
            if key == target_key:
                return value
            elif (isinstance(value, dict)):
                # If it is nested data, do recursion
                result = find(target_key, dict(value))
                
                if result is not None:
                    return result
        
        # Only raise exception when we are back in the parent dictionary
        if(data == load_config()):
            raise ConfigValueNotFound(f'Missing value for {target_key}')
    except ConfigValueNotFound as e:
        print(f'Error: {e}')

class ConfigValueNotFound(Exception):
    pass
