import base64

# Define functions
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


message = input("Enter your message: ")
key = input("Enter the key for encode'decode")
mode = input("Enter mode ( e-encode, d-decode): ").lower()

if mode == 'e':
    result = Encode(key, message)
    print(f"Encoded result -> {result}")
elif mode == 'd':
    result = Decode(key, message)
    print(f"Decoded Result -> {result}")
else:
    print("Invalid Mode")


