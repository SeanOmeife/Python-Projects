email = input("enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index:]
# domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")
