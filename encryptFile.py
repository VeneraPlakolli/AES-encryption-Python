from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from base64 import b64encode
import os.path


key_aes = input("Shtypni password-in(celesi) per enkriptim: ")
key_aes = key_aes.encode('UTF-8')
key_aes = pad(key_aes, AES.block_size)

def encryptFile(filename, key):
    with open(filename, 'rb') as enc:  
        data = enc.read()
        cypher = AES.new(key, AES.MODE_CBC)  
        cipherText = cypher.encrypt(pad(data,AES.block_size))
        iVector = b64encode(cypher.iv).decode('UTF-8')
        cipherText = b64encode(cipherText).decode('UTF-8')
        write_Enc = iVector + cipherText
    enc.close()
    return write_Enc


file_name=input("Shkruani emrin e file-t qe doni te enkriptoni: ")

try:
    exist_file = os.path.exists(file_name)
    if exist_file is True:
         print("File-n e enkriptuar e gjeni ne folderin tuaj, me emrin: "+file_name+".enc")

    #Initializing the variable with encryption function result
    encrypted_file = encryptFile(file_name, key_aes)

    #Writing the text/image to a file
    with open(file_name+".enc", 'w') as f:   
        f.write(encrypted_file)
except:
    print("File nuk ekziston ne folder")