from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:  # wb wirtebytes
#         key_file.write(key)
#
#
# write_key()

def load_key():
    with open('key.key', 'rb') as my_key:  # rb readbytes
        return my_key.read()


key = load_key()
fer = Fernet(key)


def view():
    pass


def add():
    pass


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
