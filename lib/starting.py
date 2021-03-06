from shared import *

def starting(filename):      
    print("Starting...")

    # Get the password from the input
    first = getpass.getpass("Enter the decryption password: ")
    password = first.encode()

    # Salt the password so it cannot be attacked using rainbow tables
    # It cannot be attacked using precomputed tables because those tables
    # Are unlikely to have the salt added onto the end of the tested messages
    salt = b'\xea\x0cP!\xa4\xd7\xaa{f\xf7\x97\xdd\t\xb29`'

    # KDF - key derivation function
    # Compute the key that is associated with the password
    # Using a CHF (cryptographic hash function)
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Get the key which encrypts the file
    # And create the decryption function
    key = base64.urlsafe_b64encode(kdf.derive(password))
    decrypt_function = Fernet(key)

    # Open the encrypted file for decryption
    try:
        with open('encrypted', 'rb') as encrypted_data:
            encrypted_lines = encrypted_data.read()

        decrypted_message = decrypt_function.decrypt(encrypted_lines)

        msg = decrypted_message.decode('ascii')

    except IOError as e:
        print("Encrypted file does not exist")
        exit()
    except cryptography.fernet.InvalidToken as e:
        print("Invalid passphrase")
        exit()

    print("Decrypted")
    print("Writing to plaintext file.")

    outputFile = open(os.getcwd() + '/' + filename, 'w')
    outputFile.write(msg)

    outputFile.close()

    subprocess.check_call(["shred " + os.getcwd() + "/" + "encrypted" + " --remove" ], shell=True)
    print("Done. Remember to run `python finished.py` after you are done.")
    print("Happy secure writing! :-)")

if(__name__ == "__main__"):
    starting()
