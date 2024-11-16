def generate_password(num_of_characters):
    import random
    import string

    uppercase = string.ascii_uppercase
    lowercase= string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = uppercase + lowercase + digits + symbols
    password += random.choices(all_characters, k=num_of_characters - 4)

    random.shuffle(password)

    return "".join(password)


new_password = generate_password(15)
print(new_password)