import random
import string
print("=== Password Generator ===")
length = int(input("Enter password length: "))
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
all_characters = letters + numbers + symbols
password = "".join(random.choice(all_characters) for _ in range(length))
print("\nGenerated Password:")
print(password)
