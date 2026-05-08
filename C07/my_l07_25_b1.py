import shutil
from pathlib import Path

def copyfile(source_file: str, *dest_files: str) -> object:
    """Copies a file to one or more destinations."""
    with open(source_file, 'r') as src:
        content = src.read()
    for dest_file in dest_files:
        with open(dest_file, 'w') as dest:
            dest.write(content)


def copyfile_best_c(source_file: str, *dest_files: str) -> None:
    """Copies a file to one or more destinations.

    Uses shutil.copyfile for binary-safe, efficient copying.
    Raises FileNotFoundError if source doesn't exist.
    """
    src = Path(source_file)
    if not src.exists():
        raise FileNotFoundError(f"Source file not found: {source_file!r}")
    for dest in dest_files:
        shutil.copyfile(src, dest)

def copyfile_manual_c(source_file: str, *dest_files: str) -> None:
    """Copies a file to one or more destinations (manual streaming version)."""
    with open(source_file, 'rb') as src:
        content = src.read()
    for dest_file in dest_files:
        with open(dest_file, 'wb') as dst:
            dst.write(content)

copyfile("../wcfile.txt", "wcfile_copy.txt", "wcfile_copy2.txt", "wcfile_copy3.txt", "wcfile_copy4.txt")

def copyfile_l(infilename, *args):
    for outfilename in args:
        with open(outfilename, 'w') as outfile:
            for one_line in open(infilename):
                outfile.write(one_line)

copyfile_l("wcfile.txt", "wcfile_copy5.txt", "wcfile_copy6.txt", "wcfile_copy7.txt", "wcfile_copy8.txt")