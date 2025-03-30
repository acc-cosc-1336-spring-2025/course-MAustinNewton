def get_hamming_distance(dna1: str, dna2: str) -> int:
    """Calculate the Hamming distance between two DNA strings.
    The Hamming distance is the number of differing positions in two equal-length strings."""
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be of equal length")
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance


def get_dna_complement(dna: str) -> str:
    """Get the reverse complement of a DNA string.
    'A' <-> 'T' and 'C' <-> 'G', and the result is reversed."""
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement = ""
    
    for base in dna:
        complement = complement_map[base] + complement  # Reverse while complementing

    return complement
