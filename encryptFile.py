from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from base64 import b64encode
import os.path


key_aes = input("Shtypni password-in(celesi) per enkriptim: ")
key_aes = key_aes.encode('UTF-8')
key_aes = pad(key_aes, AES.block_size)

def encryptFileFunction(FILE_NAME, algorithm_key):
    with open(FILE_NAME, 'rb') as enc:  
        data_to_read = enc.read()
        aes_cypher = AES.new(algorithm_key, AES.MODE_CBC)  
        cipherText = aes_cypher.encrypt(pad(data_to_read,AES.block_size))
        iVector = b64encode(aes_cypher.iv).decode('UTF-8')
        cipherText = b64encode(cipherText).decode('UTF-8')
        data_to_write = iVector + cipherText
    enc.close()
    return data_to_write


file_name=input("Shkruani emrin e file-t qe doni te enkriptoni: ")

try:
    exist_file = os.path.exists(file_name)
    if exist_file is True:
         print("File-n e enkriptuar e gjeni ne folderin tuaj, me emrin: "+file_name+".enc")

    #Initializing the variable with encryption function result
    encrypted_file = encryptFileFunction(file_name, key_aes)

    #Writing the text/image to a file
    with open(file_name+".enc", 'w') as f:   
        f.write(encrypted_file)
except:
    print("File nuk ekziston ne folder")