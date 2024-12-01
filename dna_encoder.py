# dna_encoder.py
DNA_MAP = {"00": "A", "01": "C", "10": "G", "11": "T"}
REVERSE_MAP = {v: k for k, v in DNA_MAP.items()}

def binary_to_dna(binary_data):
    """Convert binary string to DNA sequence."""
    return ''.join([DNA_MAP[binary_data[i:i+2]] for i in range(0, len(binary_data), 2)])

def dna_to_binary(dna_sequence):
    """Convert DNA sequence back to binary string."""
    return ''.join([REVERSE_MAP[nucleotide] for nucleotide in dna_sequence])
