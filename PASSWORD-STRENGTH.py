
import numpy as np
import string

characters = np.array(list(
    string.ascii_letters + string.digits 
))

# 2. Generate 1000 random password lengths (6 to 20)
lengths = np.random.randint(6, 21, size=1000)

# 3. Generate 1000 passwords
passwords = []

for length in lengths:
    password = ''.join(np.random.choice(characters, size=length))
    passwords.append(password)

# 4.
average_length = np.mean(lengths)

# 5. Count passwords shorter than 8 characters
short_passwords = np.sum(lengths < 8)

# 6. Display results
print("Generated passwords:", len(passwords))

print("\nPasswords:")
for password in passwords:
    print(password)

print("\nAverage password length:", average_length)

print("Passwords shorter than 8 characters:", short_passwords)
