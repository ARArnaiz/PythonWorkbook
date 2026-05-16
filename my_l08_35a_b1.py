
def config_to_dict(config_str) -> dict[str,str]:
    with open(config_str) as f:
        return { k: v for k, v in (line.strip().split("=") for line in f)}

print(config_to_dict("config_l.txt"))
print(config_to_dict("config.txt"))

def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}

print(read_config("config_l.txt"))
print(read_config("config.txt"))
