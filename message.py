from Crypto.Cipher import AES 
import base64


def pad(entry):
    padded =  entry + (16-len(entry)%16)*'['
    return padded

def enkriptimi_i_tekstit(key):
    #Getting text from user to encrypt
    plain_text = input("Shkruani tekstin qe po deshironi t'a enkriptoni: ")
    plain_text = pad(plain_text)
    plain_text = plain_text.encode('UTF-8')

    #Encryption with AES(mode ecb)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_text)
    return base64.b64encode(ciphertext).decode('UTF-8')

def dekriptimi_i_tekstit(key, ciphertext):
    #decryption with aes mode ecb
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(base64.b64decode(ciphertext.encode('utf-8')))
    unpad = data.find('['.encode('utf-8'))
    data = data[:unpad]
    return data.decode('utf-8')

#key generation
key=input("Jepni celesin qe do ta perdorni per enkriptim/dekriptim: ")
key=pad(key)
key=key.encode('UTF-8')

enkript_ose_dekript=input("\nA po deshironi te enkriptoni apo te dekriptoni tekst\n Shtyp E(Enkriptim) ose D(Dekriptim)").lower()

if enkript_ose_dekript=='e':
    #Function call
    mesazhi_i_enkriptuar = enkriptimi_i_tekstit(key)
    print(mesazhi_i_enkriptuar)

elif enkript_ose_dekript=='d':
    a=True
    mes = input("\nA po deshironi te vazhoni me dekriptim: [p/j] ").lower()

    #Checking if user wants to decrypt or not
    while a == True:
        if mes=="p":
            mesazhi_per_dekriptim = input("\nShkruani textin qe po deshironi ta dekriptoni: ")
            decript_msg = dekriptimi_i_tekstit(key,mesazhi_per_dekriptim)
            print(decript_msg)
            a=False

        elif mes=="j":
            print("Programi ka perfunduar!")
            a=False

        else:
            mes = input("\nA po deshironi te dekriptoni:\nJu lutemi shtypni j (per jo) ose p (per po):")
