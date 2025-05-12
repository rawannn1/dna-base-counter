def count_bases(dna):
    return {base: dna.upper().count(base) for base in "ATGC"}

# Example
sequence = "AAGCTCGATCG"
counts = count_bases(sequence)
print("Base Counts:", counts)
