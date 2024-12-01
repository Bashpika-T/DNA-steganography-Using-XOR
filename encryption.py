# encryption.py
import random
from dna_encoder import binary_to_dna
from utils import xor_encrypt  # Import xor_encrypt from utils

def mutate(sequence, mutation_rate=0.1, log=None):
    """Apply mutation by randomly altering DNA nucleotides and log changes."""
    sequence = list(sequence)
    if log is not None:
        log.append([])
    for i in range(len(sequence)):
        if random.random() < mutation_rate:
            original_base = sequence[i]
            sequence[i] = random.choice("ACGT".replace(sequence[i], ""))
            if log is not None:
                log[-1].append((i, original_base))
    return ''.join(sequence)

def encrypt(binary_data, key, rounds=3):
    """Encrypt binary data using reshaping, crossover, and mutation."""
    mutation_log = []
    # XOR encryption
    encrypted_binary = xor_encrypt(binary_data, key)
    # Convert binary to DNA sequence
    dna_sequence = binary_to_dna(encrypted_binary)
    # Apply mutations and log them
    for _ in range(rounds):
        dna_sequence = mutate(dna_sequence, log=mutation_log)
    return dna_sequence, mutation_log
