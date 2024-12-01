# decryption.py
from dna_encoder import dna_to_binary
from utils import xor_decrypt  # Import xor_decrypt from utils

def reverse_mutate(sequence, mutation_log):
    """Revert mutations using a mutation log."""
    sequence = list(sequence)
    for idx, original_base in mutation_log:
        sequence[idx] = original_base
    return ''.join(sequence)

def decrypt(dna_sequence, key, rounds=3, mutation_log=None):
    """Decrypt DNA sequence."""
    # Reverse mutation using the log
    for _ in range(rounds):
        if mutation_log:
            dna_sequence = reverse_mutate(dna_sequence, mutation_log.pop())
    # Convert DNA to binary
    binary_data = dna_to_binary(dna_sequence)
    # XOR decryption
    return xor_decrypt(binary_data, key)
