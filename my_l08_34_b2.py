import string


def word_length_set(filename) -> set[int]:
    with open(filename) as f:
        return {
            len(word if word[-1].isalnum() else word[:-1])
            for line in f
            for word in line.split()}


print(word_length_set("wcfile.txt"))


def word_length_set_c(filename) -> set[int]:
    with open(filename) as f:
        return {
            len(word.strip(string.punctuation))
            for line in f
            for word in line.split()
            if word.strip(string.punctuation)  # exclude words that are pure punctuation
        }

print(word_length_set_c("wcfile.txt"))

def word_lengths(filename):
    return {len(one_word)
            for one_line in open(filename)
            for one_word in one_line.split()}


print(word_lengths("wcfile.txt"))
