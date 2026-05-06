# Read through a text file on disk. Use a dict to track how many
# words of each length are in the file—that is, how many three-letter
# words, four-letter words, five-letter words, and so on.
# Display your results.

def freq_by_length(filename)-> dict:
    freq_dict_length = {}
    with open(filename, "r") as f:
        for line in f:
            tokens = line.strip().lower().split()
            for token in tokens:
                freq_dict_length[len(token)] = freq_dict_length.get(len(token), 0) + 1
    output = dict(sorted(freq_dict_length.items(), reverse=True))
    return output

print(len(freq_by_length("../article001.txt")))
print(freq_by_length("../article001.txt"))