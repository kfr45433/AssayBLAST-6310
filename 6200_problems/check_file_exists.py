from pathlib import Path
import os
def read_fasta(file_path :str):
    print("Argument:", repr(file_path))
    print("Working directory:", os.getcwd())
    print("Resolved path:", Path(file_path).resolve())
    print("Exists:", Path(file_path).exists())
    path = Path(file_path)

    print("Looking for: ", path.resolve())
    print("Exists:", path.exists())
    with path.open() as f:
        for line in f:
            print(line.strip())

read_fasta("hello.txt")