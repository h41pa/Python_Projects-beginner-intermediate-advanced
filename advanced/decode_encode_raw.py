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

# Get user input
message = input("Enter the message: ")
key = input("Enter the key: ")
mode = input("Enter mode (e-encode, d-decode): ")

# Process input based on mode
if mode == 'e':
    result = Encode(key, message)
    print(f"Encoded Result: {result}")
elif mode == 'd':
    result = Decode(key, message)
    print(f"Decoded Result: {result}")
else:
    print("Invalid Mode")
