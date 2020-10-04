def encode(pText, key):
    cText = ""
    for i in range(0, len(pText)):
        cText += encodeChar(pText[i], key[i])

    return cText

def encodeChar(pText, key):
    cNum = (charToNum(pText) + charToNum(key)) % 26
    cText = numToChar(cNum)
    return cText

def charToNum(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num += 1
    return num

def numToChar(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num+1]


pt = str(input("Enter plain text:")).upper()
ky = str(input("Enter key:")).upper()
print(encode(pt, ky))
