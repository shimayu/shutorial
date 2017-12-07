message = ""
prefix = "TWCTF{"
message += prefix
for i in range(15):
    message += "*"
message += '|'

with open('encrypted.txt', "r") as f:
    enc = f.read().strip()
enc = enc.decode('hex')

encrypted = []
for c in enc:
    encrypted.append(ord(c))

key = []
for i in range(0, len(prefix)):
    tmp = encrypted[i+1] - ord(prefix[i]) - encrypted[i]
    key.append(chr(tmp % 128))

for i in range(28, 35):
    tmp = encrypted[i+1] - encrypted[i] - ord(key[i%13])
    key.append(chr(tmp % 128))

for i in range(len(key)):
    message += key[i]

plane_text = ""
for i in range(len(message)):
    tmp = encrypted[i+1] - encrypted[i] - ord(key[i % 13])
    plane_text += chr(tmp % 128)

print(plane_text)
