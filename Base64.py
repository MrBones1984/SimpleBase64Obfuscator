import base64


def encode_base64(text):
    """Encodes plain text to Base64."""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def decode_base64(encoded_text):
    """Decodes Base64 back to plain text."""
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


if __name__ == "__main__":
    while True:
        choice = input("Choose an option:\n1. Encode to Base64\n2. Decode from Base64\n3. Exit\n> ")

        if choice == "1":
            text = input("Enter text to encode: ")
            print("Encoded:", encode_base64(text))
        elif choice == "2":
            encoded_text = input("Enter Base64 to decode: ")
            try:
                print("Decoded:", decode_base64(encoded_text))
            except Exception as e:
                print("Invalid Base64 input:", e)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
