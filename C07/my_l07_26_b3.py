from typing import Callable, TextIO

def transform_lines(function: Callable, infile: TextIO, outfile: TextIO)-> None:
    """Apply a transformation function to each line in infile and write to outfile."""
    with open(infile, 'r') as input_file, open(outfile, 'w') as output_file:
        for line in input_file:
            transformed_line = function(line)
            output_file.write(transformed_line)


def transform_lines_c(function: Callable[[str], str], infile: TextIO, outfile: TextIO) -> None:
    """Apply a transformation function to each line in infile and write to outfile."""
    for line in infile:
        outfile.write(function(line))
    # Don't use open() again—parameters are already file objects!

def transform_lines_l(f, infilename, outfilename):
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for one_line in infile:
            outfile.write(f(one_line))

def transform_lines_l_c(f: Callable[[str], str], infilename: str, outfilename: str) -> None:
    """Apply function f to each line in infilename and write results to outfilename."""
    with open(infilename) as infile, open(outfilename, 'w') as outfile:
        for line in infile:
            outfile.write(f(line))
