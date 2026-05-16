
def config_to_dict_conv(config_str) -> dict[str,str]:
    with open(config_str) as f:
        return { k: int(v) if v.isdigit() else v for k, v in (line.strip().split("=") for line in f) }

print(config_to_dict_conv("config_l.txt"))
print(config_to_dict_conv("config.txt"))

def config_to_dict_filter(config_str) -> dict[str,str]:
    with open(config_str) as f:
        return { k: int(v) for k, v in (line.strip().split("=") for line in f) if v.isdigit() }

print(config_to_dict_filter("config_l.txt"))
print(config_to_dict_filter("config.txt"))

def read_config(filename):
    return {one_line.split('=')[0]: int(one_line.split('=')[1].strip())
            for one_line in open(filename)
            if one_line.split('=')[1].strip().isdigit()}

print(read_config("../config_l.txt"))
print(read_config("../config.txt"))