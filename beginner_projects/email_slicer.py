def email_slicer():
    while True:
        print("\t Welcome to email slicer!\n")

        email_input = input("Input your email adress: ")
        (username, domain) = email_input.split("@")
        (domain, extension) = domain.split(".")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print(f"Extension: {extension}")

email_slicer()
