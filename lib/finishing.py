from shared import *

def finishing(filename):
    print("Closing up...")

    # Open the plaintext file for reading
    try:
        journal_file = open(os.getcwd() + '/' + filename, 'r')
        # Read the file
        journal_file_contents = journal_file.readlines()
        journal_file.close()
    except IOError as e:
        print("Error: File '" + filename + "' does not exist in current directory")
        exit()

    # Get the password from the input
    first = getpass.getpass("Enter the encryption key password: ")
    second = getpass.getpass("Enter it again: ")
    if(first != second):
        print("Passwords do not match")
        exit()
        
    # Base64 encode the password
    password = first.encode()

    kdf = getKeyDerivationFunction()

    # Get the key which encrypts the file
    key = base64.urlsafe_b64encode(kdf.derive(password))
    encrypt_function = Fernet(key)

    print("Encoding the message")
    # Encode the message from the file in Base64
    message = str(journal_file_contents)
    encoded_message = message.encode()

    # Encrypt the message
    encrypted_message = encrypt_function.encrypt(encoded_message)

    # Write the encrypted file
    outputFile = open(os.getcwd() + '/' + 'encrypted', 'w+')
    outputFile.write(encrypted_message)
    print("Wrote to encrypted file")

    # Delete the journal file
    filePath = os.getcwd() + '/' + filename
    subprocess.check_call(["srm", filePath])
    print("Done!")
    
if(__name__ == "__main__"):
    finished()
