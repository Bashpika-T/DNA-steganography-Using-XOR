# utils.py
import random

def xor_encrypt(binary_data, key):
    """XOR binary data with a key."""
    key = key * (len(binary_data) // len(key)) + key[:len(binary_data) % len(key)]
    return ''.join(str(int(b) ^ int(k)) for b, k in zip(binary_data, key))

def xor_decrypt(binary_data, key):
    """XOR decryption (same as encryption)."""
    return xor_encrypt(binary_data, key)

def reshape_sequence(sequence, length):
    """Reshape a sequence into smaller parts."""
    return [sequence[i:i+length] for i in range(0, len(sequence), length)]

def generate_key(length):
    """Generate a random binary key."""
    return ''.join(random.choice("01") for _ in range(length))

def xor_encrypt(binary_data, key):
    """XOR binary data with a key."""
    key = key * (len(binary_data) // len(key)) + key[:len(binary_data) % len(key)]
    return ''.join(str(int(b) ^ int(k)) for b, k in zip(binary_data, key))

def xor_decrypt(binary_data, key):
    """XOR decryption (same as encryption)."""
    return xor_encrypt(binary_data, key)


