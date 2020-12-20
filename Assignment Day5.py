from cryptography.fernet import Fernet


def generatePassKey():
    key = Fernet.generate_key()
    print(key)
    print(type(key))
    abc = open("passkey.key", "wb")
    abc.write(key)
    abc.close()


def getMyKey():
    abc = open("passkey.key", "rb")
    return abc.read()


def getContentFromUser():
    message = (input("Enter the content you want to encrypt in your python script"))
    b = bytes(message, 'utf-8')
    #b = message.encode('utf-8')
    return b


def encryptMessage(message_normal):
    key = getMyKey()
    k = Fernet(key)
    encrypted_message = k.encrypt(message_normal)
    return encrypted_message


def decryptMessage(message_secret):
    key = getMyKey()
    k = Fernet(key)
    decrypted_message = k.decrypt(message_secret)
    return decrypted_message


message1 = getContentFromUser()
generatePassKey()
dec = getMyKey()
encryptMessage(message1)
decryptMessage(b'cZl8Uw0tblS4B67NHnMfzpqiWG8239q3uOMw-bRukrI=')
