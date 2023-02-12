
def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
def decrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = (result,s)
 
        if (char.isupper()):
            result += chr((ord(char) + s + 65) % 26 - 65)
 
        else:
            result += chr((ord(char) + s + 97) % 26 - 97)
 
    return result
 

text = "THe quick"
s = 3


a = encrypt(text,s)
print ("Cipher: " + encrypt(text,s))
#print(decrypt(a,s))