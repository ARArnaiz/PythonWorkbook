from collections import deque

def get_final_line(filename)-> str:
    """Given a filename, returns the final line in that file."""
    with open(filename) as f:
       return f.readlines()[-1]

def get_final_line_l(filename):
    """Given a filename, returns the final line in that file."""
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line

def get_final_line_c(filename: str) -> str:
    """Given a filename, returns the final line in that file. Uses stream,
    no file loaded in memory"""
    with open(filename) as f:
        for line in f:
            pass
        return line

def get_final_line_c2(filename: str) -> str:
    """" deque(f, maxlen=1) streams the file and keeps only the last line at
    any moment — never loads more than one line into memory regardless of file size."""
    
    with open(filename) as f:
        return deque(f, maxlen=1).pop()

print(get_final_line("../apache_logs.txt"))
print(get_final_line_l("../apache_logs.txt"))
print(get_final_line_c("../apache_logs.txt"))
print(get_final_line_c2("../apache_logs.txt"))