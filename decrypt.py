from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass


key = getpass.getpass('Shkruaje password: ')
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

file_name=input("Shkruani emrin e file qe doni te dekriptoni: ")
with open(file_name, 'r') as entry:  
    try:
        data = entry.read()
        length = len(data)
        iv = data[:24]
        iv = b64decode(iv)
        ciphertext = data[24:length]
        ciphertext = b64decode(ciphertext)
        cipher = AES.new(key,AES.MODE_CBC,iv)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted,AES.block_size)
        with open('test.txt.dec','wb') as data:  
            data.write(decrypted)
        data.close()
        print("File i dekriptuar eshte ne folder!")
    except(ValueError,KeyError):
        print('password-i gabim')
