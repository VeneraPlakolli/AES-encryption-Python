from Crypto.Cipher import AES 
import base64


def pad(entry):
    padded =  entry + (16-len(entry)%16)*'['
    return padded

def encrypt(key):
    #Getting text from user to encrypt
    plain_text = input("Shkruani tekstin qe po doni me e enkript: ")
    plain_text = pad(plain_text)
    plain_text = plain_text.encode('UTF-8')

    #Encryption with AES(mode ecb)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_text)
    return base64.b64encode(ciphertext).decode('UTF-8')

def decrypt(key, ciphertext):
    #decryption with aes mode ecb
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(base64.b64decode(ciphertext.encode('utf-8')))
    unpad = data.find('['.encode('utf-8'))
    data = data[:unpad]
    return data

#key generation
key='12345'
key=pad(key)
key=key.encode('UTF-8')

#Function call
mesazhi_i_enkriptuar = encrypt(key)
print(mesazhi_i_enkriptuar)

a=True
mes = input("A po deshironin me e dekript: [p/j] ").lower()

#Checking if user wants to decrypt or not
while a == True:
    if mes=="p":
        decript_msg = decrypt(key,mesazhi_i_enkriptuar)
        print(decript_msg)
        a=False

    elif mes=="j":
        print("Programi ka perfunduar!")
        a=False

    else:
     mes = input("A po deshironin me e dekript:\nJu lutemi shtypni j (per jo) ose p (per po):")
