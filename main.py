import re

mRNA = input("Enter a mRNA sequence: ").upper()


def find_start(sequence) -> int:
    regex = re.compile("AUG")
    match = regex.search(sequence)
    if match:
        return match.start()
    else:
        return -1


def find_stop(sequence):
    regex = re.compile("UAA|UGA|UAG")
    match = regex.search(sequence)
    if match:
        return match.start()
    else:
        return -1


def rna_to_aa(rna_seq):
    aa_seq = ["Met"]
    for p in range(3, len(rna_seq), 3):
        codon = rna_seq[p : p + 3]
        if codon == "UUU" or codon == "UUC":
            aa_seq.append("-Phe")
        elif (
            codon == "UUA"
            or codon == "UUG"
            or codon == "CUU"
            or codon == "CUC"
            or codon == "CUA"
            or codon == "CUG"
        ):
            aa_seq.append("-Leu")
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            aa_seq.append("-Ile")
        elif codon == "GUU" or codon == "GUC" or codon == "GUA" == codon == "GUG":
            aa_seq.append("-Val")
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            aa_seq.append("-Ser")
        elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            aa_seq.append("-Pro")
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            aa_seq.append("-Thr")
        elif codon == "GCU" or codon == "GCU" or codon == "GCA" or codon == "GCG":
            aa_seq.append("-Ala")
        elif codon == "UAU" or codon == "UAC":
            aa_seq.append("-Tyr")
        elif codon == "CAU" or codon == "CAC":
            aa_seq.append("-His")
        elif codon == "CAA" or codon == "CAG":
            aa_seq.append("-Gln")
        elif codon == "AAU" or codon == "AAC":
            aa_seq.append("-Asn")
        elif codon == "AAA" or codon == "AAG":
            aa_seq.append("-Lys")
        elif codon == "GAU" or codon == "GAC":
            aa_seq.append("-Asp")
        elif codon == "GAA" or codon == "GAG":
            aa_seq.append("-Glu")
        elif codon == "UGU" or codon == "UGC":
            aa_seq.append("-Cys")
        elif codon == "UGG":
            aa_seq.append("-Trp")
        elif (
            codon == "CGU"
            or codon == "CGC"
            or codon == "CGA"
            or codon == "CGG"
            or codon == "AGA"
            or codon == "AGG"
        ):
            aa_seq.append("-Arg")
        elif codon == "AGU" or codon == "AGC":
            aa_seq.append("-Ser")
        elif codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
            aa_seq.append("-Gly")
        else:
            print(f"Error: invalid sequence {codon}")
            exit(1)

    print(f'Your mRNA codes for the amino acid sequence: {"".join(aa_seq)}')


def main():
    start = find_start(mRNA)
    end = find_stop(mRNA)

    if start < 0:
        print("Error: could not find start")
        exit(1)
    elif end < 0:
        print("Error: could not find end")
        exit(1)

    rna_to_aa(mRNA[start:end])


if __name__ == "__main__":
    main()
