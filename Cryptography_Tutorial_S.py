import string
# Secret Message Encoder and Decoder


# Caesar Cipher (Easy)
def caesar_cipher(text, shift, mode="encode"):
    """
    A function to encode or decode a text using the Caesar cipher.

    Parameters:
    - text (str): The input text to encode or decode.
    - shift (int): The number of positions to shift letters by.
    - mode (str): Determines whether to "encode" (shift forward) or "decode" (shift backward).
                  Default is "encode".

    Returns:
    - str: The transformed text after applying the Caesar cipher.
    """
    result = ""
    #your code goes here
    return result

# Substitution cipher (Difficult)
def create_substitution_mapping(key):
    # Define a variable 'alphabet' containing all lowercase letters (a to z)
    alphabet = string.ascii_lowercase 
    # Create a dictionary where each letter of 'alphabet' maps to the corresponding letter in 'key'
    # This is the first substitution mapping (alphabet -> key)
    # It loops through each letter in 'alphabet' and pairs it with the same index in 'key'
    forward_mapping = {alphabet[i]: key[i] for i in range(26)}
    reverse_mapping = {key[i]: alphabet[i] for i in range(26)}
    return forward_mapping, reverse_mapping


def substitution_cipher(text, key, mode="encode"):
    """
    A function to encode or decode text using a substitution cipher.

    Parameters:
    - text (str): The input text to encode or decode.
    - key (str): A 26-character string representing the substitution key.
    - mode (str): Determines whether to "encode" (use forward mapping) or "decode" (use reverse mapping).
                  Default is "encode".

    Returns:
    - str: The transformed text after applying the substitution cipher.
    """
    result=""
    #your code goes here
    return result


# Vigenere Cipher (Complex)
def vigenere_cipher(text, keyword, mode="encode"):
    """
    A function to encode or decode text using the Vigenère cipher.

    Parameters:
    - text (str): The input text to encode or decode.
    - keyword (str): The keyword used for shifting each letter.
    - mode (str): Determines whether to "encode" (shift forward) or "decode" (shift backward).
                  Default is "encode".

    Returns:
    - str: The transformed text after applying the Vigenère cipher.
    """
    #Your code goes here...
    result = []
    return result

# Menu for the program
def main():
    print("Welcome to the Secret Message Encoder and Decoder!")
    while True:
        print("\nChoose an option:")
        print("1. Caesar Cipher")
        print("2. Substitution Cipher")
        print("3. Vigenere Cipher")
        print("4. Exit")

        choice = input("Your choice of cipher: ")
        #Run Ceaser Cipher
        if choice == "1":
            print("Choose an option:")
            print("1. Encode")
            print("2. Decode")
            choice2 = input("Your choice:")
            if choice2 =="1":
                message = input("Enter the message to encode: ")
                shift = int(input("Enter the shift value (1-25): "))
                encoded_message = caesar_cipher(message, shift, mode="encode")
                print(f"Encoded Message: {encoded_message}")
            elif choice2 == "2":
                message = input("Enter the message to decode: ")
                shift = int(input("Enter the shift value (1-25): "))
                decoded_message = caesar_cipher(message, shift, mode="decode")
                print(f"Decoded Message: {decoded_message}")
        #Run Substitution Cipher
        elif choice == "2":
            print("Choose an option:")
            print("1. Encode")
            print("2. Decode")
            choice2 = input("Your choice:")
            if choice2 =="1":
                key = "keywordabcfghijlmnpqstuvxz"  # Example key (randomized alphabet)
                message = input("Enter the message to encode: ")
                print(f"Key:{key}")
                encoded = substitution_cipher(message, key, mode="encode")
                print(f"Encoded Message: {encoded}")
            elif choice2 == "2":
                message = input("Enter the message to decode: ")
                decoded = substitution_cipher(message, key, mode="decode")
                decoded = substitution_cipher(encoded, key, mode="decode")
                print(f"Decoded Message: {decoded}")
            else:
                print("Invalid choice. Please try again.")
        #Run Vignere Cipher
        elif choice == "3":
            print("Choose an option:")
            print("1. Encode")
            print("2. Decode")
            choice2 = input("Your choice:")
            if choice2 =="1":
                message = input("Enter the message to encode: ")
                keyword = input("Enter keyword: ")
                encoded = vigenere_cipher(message, keyword, mode="encode")
                print(f"Encoded Message: {encoded}")
            elif choice2 == "2":
                message = input("Enter the message to decode: ")
                keyword = input("Enter keyword: ")
                decoded = vigenere_cipher(encoded, keyword, mode="decode")
                print(f"Decoded Message: {decoded}")
        elif choice == "4":
            print(f"Goodbye, Happy Coding!")
            break;
if __name__ == "__main__":
    main()