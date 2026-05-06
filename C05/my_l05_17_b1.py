#Mine
def pull_ips(file) -> set:
    with open(file, "r") as l:
        # for line in l:
        #     line = line.split()[0]
        #     ips.add(line)
        ips = {line.split()[0] for line in l}
    return ips

# Lerner
def different_ips(filename):
    return {one_line.split()[0] for one_line in open(filename)}

# Claude
def pull_ips2(filename: str) -> set:
    with open(filename) as f:
        return {line.split()[0] for line in f}

print(pull_ips("../apache_logs.txt"))
print(different_ips("../apache_logs.txt"))
print(pull_ips2("../apache_logs.txt"))
