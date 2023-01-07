from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode


key = input('Please insert your password: ')
key = key.encode('UTF-8')
key = pad(key, AES.block_size)

def encrypt(filename, key):
    with open(filename, 'rb') as entry:  
        data = entry.read()
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(data,AES.block_size))
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        to_write = iv + ciphertext
    entry.close()
    return to_write

file_name=input("Shkruni emrin e file qe doni te enkriptoni : ")

encrypted_file = encrypt(file_name, key)


with open(file_name+".enc", 'w') as f:   
    f.write(encrypted_file)