import random 

def password_generator(length=16):
    special_chr = ['!', '@', '#', '$', '%', '&']

    upper = chr(random.randint(65, 90))
    another_upper = chr(random.randint(65, 90))

    lower = chr(random.randint(97, 122))
    another_lower = chr(random.randint(97, 122))
    special = random.choice(special_chr)
    another_special = random.choice(special_chr)
    digit = str(random.randint(10000, 99999))
    another_digit = str(random.randint(100, 999))

    # making passwords
    join_pass = upper + lower + special + digit + another_special + another_lower + another_upper + another_digit
    generate = random.sample(join_pass, length)
    result = ''.join(generate)
    return result

print("\n---Python Password Generator---".upper())
user_input = int(input("\nHow many numbers password you want? "))
if user_input > 12:
    print("Sorry! We can only generate 12 characters passwords.")
else:
    pass
output = password_generator(user_input)
print(f"Your Password is :  {output}")
