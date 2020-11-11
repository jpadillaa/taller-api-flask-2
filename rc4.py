def text_to_bytes(message: str):    
    byteList = []
    
    for byte in message:        
        byteList.append(ord(byte))
        
    return byteList

def hex_to_bytes(encrypted_message: str):    
    byteList = []
    
    for i in range(0, len(encrypted_message), 2):
        byte = encrypted_message[i:i+2]        
        byteList.append(int('0X' + byte, 16))
        
    return byteList

def bytes_to_text(ByteList):
    s = ''
    for byte in ByteList:
        s += chr(byte)
    return s

def bytes_to_hex(ByteList):
    l = []
    for byte in ByteList:
        hexStr = '0' + hex(byte)[2:]
        l.append(hexStr[-2:].upper())
    return l


def crypt(PlainBytes, KeyBytes):
    
    keystreamList = []
    cipherList = []

    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + KeyBytes[i % keyLen]) % 256
        t = S[i]
        S[i] = S[j]
        S[j] = t

    i = 0
    j = 0
    
    for m in range(plainLen):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        keystreamList.append(k)
        cipherList.append(k ^ PlainBytes[m])
	
    return keystreamList, cipherList

def encrypt(message, Key):
    KeyBytes = text_to_bytes(Key)
    PlainBytes = text_to_bytes(message)    
    KeystreamBytes, CipherBytes = crypt(PlainBytes, KeyBytes)
    
    return bytes_to_hex(CipherBytes)

def decrypt(message, Key):
    CipherBytes = hex_to_bytes(message)
    KeyBytes = text_to_bytes(Key)
    KeystreamBytes, PlainBytes = crypt(CipherBytes, KeyBytes)
    
    return bytes_to_text(PlainBytes)
    