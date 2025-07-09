email = input("enter your email: ")

# Find the position of the "@" symbol in the email address
index = email.index("@")

# Extract the username (everything before "@")
username = email[:index]

# Extract the domain (everything from "@" onward, including "@")
domain = email[index:]

# Alternative: Extract the domain without the "@" onward, including "@"
# domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")
