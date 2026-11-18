def to_rdna(dna_strand):
    rna_strand = ""

    for char in rna_strand:
        if char not in "GCTA":
            raise ValueError("Invalid character in DNA strand")

        if char == "G":
            rna_strand += "C"
        elif char == "C":
            rna_strand += "G"
        elif char == "T":
            rna_strand += "A"
        elif char == "A":
            rna_strand += "U"

            