from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass


key = getpass.getpass('Shkruaje password-in: ')
key = key.encode('UTF-8')
key = pad(key,AES.block_size)

file_name=input("Shkruani emrin e file-t qe doni te dekriptoni: ")
with open(file_name, 'r') as entry:  
    try:
        data = entry.read()
        length = len(data)
        iVector = data[:24]
        iVector = b64decode(iVector)
        ciphertext = data[24:length]
        ciphertext = b64decode(ciphertext)
        cipher = AES.new(key,AES.MODE_CBC,iVector)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted,AES.block_size)
        with open(file_name+".dec",'wb') as data:  
            data.write(decrypted)
        data.close()
        print("File i dekriptuar"+file_name+".dec eshte ne folder!")
    except(ValueError,KeyError):
        print('password-i gabim')
