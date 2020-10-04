import string

alpha = list(string.ascii_uppercase)

sent = input("Enter PT:")
key = input("Enter key:")

sent = sent.strip().upper()
key = key.upper()

en_text = ""

for i in range(len(sent)):
    en_text += alpha[(alpha.index(sent[i])+alpha.index(key[i%len(key)]))%26]

print(en_text)