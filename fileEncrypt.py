from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from base64 import b64encode


key = input("Shtypni password-in(celesi) per enkriptim:")
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

def encrypt(filename, key):
    with open(filename, 'rb') as entry:  
        data = entry.read()
        cipher = AES.new(key, AES.MODE_CBC)  
        ciphertext = cipher.encrypt(pad(data,AES.block_size))
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        to_write = iv + ciphertext
    entry.close()
    return to_write


file_name=input("Shkruni emrin e file qe doni te enkriptoni : ")
print("Fajllin e enkriptuar me emrin "+file_name+".enc e gjeni ne folderin tuaj!")

#Initializing the variable with encryption function result
encrypted_file = encrypt(file_name, key)

#Writing the text/image to a file
with open(file_name+".enc", 'w') as f:   
    f.write(encrypted_file)