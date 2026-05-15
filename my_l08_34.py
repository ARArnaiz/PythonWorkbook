
def get_sv(filename: str, lang: str) -> set:

    with open(filename) as file:
        if lang == 'en':
            vowels = set('aeiou')
        else:
            raise ValueError(f"Unsupported language: {lang}")

        result = { word.strip()
                 for word in file
                 if vowels.issubset(set(word.lower()))
                 }
    print(f"There are {len(result)} words that contain all vowels.")
    return result

en_results_sv = get_sv('en_words.txt', 'en')
print(len(en_results_sv))

def get_sv_l(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
             for word in open(filename)
             if vowels < set(word.lower())}

en_results_sv = get_sv_l('en_words.txt')
print(len(en_results_sv))

def get_sv_vg(filename: str, lang: str) -> set:

    with open(filename, encoding='utf-8') as file:
        if lang == 'en':
            vowel_groups = [{'a'}, {'e'}, {'i'}, {'o'}, {'u'}]
        elif lang == 'es':
            vowel_groups = [
                {'a', 'á'},
                {'e', 'é'},
                {'i', 'í'},
                {'o', 'ó'},
                {'u', 'ú', 'ü'},
            ]
        else:
            raise ValueError(f"Unsupported language: {lang}")

        def has_all_vowels(word):
            letters = set(word.lower())
            return all(group & letters for group in vowel_groups)

        result = {word
                  for line in file
                  for word in line.split()
                  if has_all_vowels(word)}

    print(f"There are {len(result)} words that contain all vowels.")
    return result

sv_result = get_sv_vg('es_words.txt', 'es')

# with open('SP_DUMP_cleaned.txt', encoding="utf-16") as f:
#     content = f.read()
#
# with open('es_words_sv.txt', "w", encoding="utf-8") as f:
#     for word in sv_result:
#         f.write(word + '\n')