def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")

    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return round(differences / len(list1), 5)


def get_p_distance_matrix(dna_lists):
    n = len(dna_lists)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0.0)
            else:
                row.append(get_p_distance(dna_lists[i], dna_lists[j]))
        matrix.append(row)

    return matrix
