def ini_to_dict(filename: str) -> dict:
    with open(filename) as f:
        return {key.strip(): value.strip()
                for key, value in [line.strip().split("=", 1)
                                   for line in f if "=" in line]}

print(ini_to_dict("config.txt"))

def ini_to_dict_c(filename: str) -> dict:
    with open(filename) as f:
        return {
            key.strip(): value.strip()
            for line in f
            if "=" in line and not line.lstrip().startswith("#")
            for key, value in [line.split("=", 1)]
        }

print(ini_to_dict_c("config.txt"))

# str.partition("=") is even cleaner than split("=", 1) here — it always returns exactly
# three parts (before, sep, after) regardless of whether = is present, so there's no unpack
# risk at all. The "=" in line guard is still worth keeping for clarity and to skip comment
# lines before they're parsed.

def _parse_line(line: str) -> tuple[str, str]:
    key, _, value = line.partition("=")
    return key.strip(), value.strip()

def ini_to_dict_c2(filename: str) -> dict:
    with open(filename) as f:
        return dict(
            _parse_line(line)
            for line in f
            if "=" in line and not line.lstrip().startswith("#")
        )

print(ini_to_dict_c2("config.txt"))

def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}

print(read_config("config.txt"))