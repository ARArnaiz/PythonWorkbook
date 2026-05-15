import string

names = [ "Claudia Sibila Zegarra", "Alfredo Arnaiz Fernández-Concha", "Camila Arnaiz Sibila", "Alfredo Arnaiz Sibila"]

def chars_in_names(lst) -> set[str]:
    return { char
             for name in lst
             for char in name.lower()
             if char in string.ascii_letters}

print(sorted(chars_in_names(names)))

def chars_in_names_c(lst) -> set[str]:
    return {
        char
        for name in lst
        for char in name.lower()
        if char.isalpha()        # Unicode-aware: catches é, á, ñ, ü...
    }

print(sorted(chars_in_names_c(names)))

def letters_in_names(list_of_names):
    return {one_letter
            for one_letter in ''.join(list_of_names)
            if one_letter in string.ascii_letters}

print(sorted(letters_in_names(names)))