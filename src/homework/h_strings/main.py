def get_hamming_distance(dna1: str, dna2: str) -> int:
    """Calculate the Hamming distance between two DNA strings"""
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be of equal length")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance


def get_dna_complement(dna: str) -> str:
    """Get the reverse complement of a DNA string
    'A' <-> 'T' and 'C' <-> 'G', and the result is reversed."""
    complement = ""

    for i in range(len(dna) - 1, -1, -1):  # Reverse using loop
        base = dna[i]
        if base == 'A':
            complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'

    return complement
