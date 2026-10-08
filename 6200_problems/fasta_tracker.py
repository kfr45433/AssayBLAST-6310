"""find the lengths of DNA sequences in a fasta file."""
def find_lengths(file_path :str):
    """function finds the lengths of the DNA sequences.
        @param: file_path, or the path to the file to be read
        @return: None, since this prints to console.
    """
    # since this function accepts a file_path as a string, open it -- normally you should wrap this in a try...except block for more robustness
    # but we'll assume the file_path given to the function is structured like a .fasta file or something
    header :str = ""
    sequence :list[str] = []
    with open(file_path, encoding="utf-8") as handle:
        for line in handle:
            # normalize first, remove any trailing newlines
            line = line.rstrip()
            if line.startswith(">"):
                # we've hit a new header, so we must process the previous sequence.
                # check: is the sequence var empty? if it's not, let's print the len to console.
                if header: #check it's not empty before processing the previous sequence
                    seq = "".join(sequence)
                    print(header)
                    print(len(seq))
                # start another record again
                header = line
                sequence = []
            else:
                # add the line to the sequence
                sequence.append(line)
    if header:
        seq = "".join(sequence)
        print(header)
        print(len(seq))

if __name__=="__main__":
    find_lengths("hello.txt")