# main.py
from dna_encoder import binary_to_dna, dna_to_binary
from encryption import encrypt
from decryption import decrypt
from utils import generate_key

def main():
    # User Input
    text = input("Enter the text to encrypt: ")
    binary_data = ''.join(format(ord(c), '08b') for c in text)
    
    # Key Generation
    key = generate_key(len(binary_data))
    print(f"Generated Key: {key}")
    
    # Encryption
    encrypted_dna, mutation_log = encrypt(binary_data, key, rounds=3)
    print(f"Encrypted DNA Sequence: {encrypted_dna}")
    
    # Decryption
    decrypted_binary = decrypt(encrypted_dna, key, rounds=3, mutation_log=mutation_log)
    decrypted_text = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8))
    print(f"Decrypted Text: {decrypted_text}")
    
if __name__ == "__main__":
    main()
