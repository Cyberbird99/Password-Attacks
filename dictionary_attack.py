import crypt

def test_password(hashed_password, algorithm_salt, plaintext_password):
    # Generate a hash using the provided algorithm/salt and plaintext password.
    crypted_password = crypt.crypt(plaintext_password, algorithm_salt)

    # Compare the hashed password to the generated hash.
    return hashed_password == crypted_password

def read_dictionary(dictionary_file):
    # Open the specified dictionary file and store its contents in a variable.
    with open(dictionary_file, "r") as f:
        return f.read().splitlines()

# Load the dictionary file and request the hashed password along with the algorithm and salt.
password_dictionary = read_dictionary("top100.txt")
hashed_password = input("What is your hashed password? ")
algorithm_salt = input("What is your algorithm and salt? ")

# For each password in the dictionary file, compare it to the hashed password
for password in password_dictionary:
    result = test_password(hashed_password, algorithm_salt, password)
    if result:
        # If a match is found, print it and quit
        print("Match found: {0}".format(password))
        break
else:
    print("No match found.")