# DNA-Based Steganography (D-GET)

This repository implements a **DNA-Based Steganography** project using the **DNA Genetic Encryption Technique  described in our [research paper](https://ieeexplore.ieee.org/abstract/document/10370766). 

The technique involves encoding binary data into DNA sequences and securing it with multiple layers of encryption, including mutation, crossover, and reshaping. This project demonstrates both encryption and decryption of text data.

---

## **How It Works**
1. **Encoding Binary to DNA**: Input text is converted to binary and mapped to DNA bases (A, C, G, T).
2. **Encryption**:
   - XOR-based encryption is applied using a randomly generated key.
   - DNA sequences are mutated for added security.
   - Multiple encryption rounds enhance robustness.
3. **Decryption**:
   - Reverses mutation, reshaping, and XOR operations to retrieve the original text.

---

## **Features**
- Converts input text into DNA-like sequences for encryption.
- Implements genetic operations such as mutation and crossover for multi-layer security.
- Supports decryption to recover original text data.
- Uses randomly generated keys for XOR encryption.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/DNA-Steganography.git
   cd DNA-Steganography
