# Import the base64 module, which provides functions for working with base64 encoding.
# Base64 encoding is used to encode binary data to an ASCII string format.
import base64

# Define a function named 'decode_pass' that takes a 'password' argument.
# This function is responsible for decoding a base64-encoded string.
def decode_pass(password):
    # Use the base64 module to decode the provided base64 string.
    # The result is a bytes object which contains the original binary data.
    decode_bytes = base64.b64decode(password)
    
    # Decode the bytes object to a string using the default encoding (UTF-8).
    # This assumes that the binary data was originally a UTF-8 encoded string.
    decode_data = decode_bytes.decode()
    
    # Print the decoded string, which is the original password before it was encoded.
    print(f"decoded password: {decode_data}")

# Prompt the user to enter a base64-encoded string and store their input in 'encode_string'.
encode_string = input("enter the base64 string: ")

# Call the 'decode_pass' function with the user-provided base64-encoded string.
# The function will decode and print the original string.
decode_pass(encode_string)


    