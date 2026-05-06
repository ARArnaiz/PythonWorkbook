import json
from pathlib import Path
_HERE = Path(__file__).parent

def psswrd_2_json(infile: str, outfile: str) -> None:
    with open(infile) as f, open(outfile, "w") as j:
        output = []
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            output.append(tuple(line.strip().split(':')))
        json.dump(output, j, indent=2)

def psswrd_2_json_c(infile: str, outfile: str) -> None:
    """Reads a passwd-style file and writes its contents as JSON to outfile."""
    with open(_HERE / infile) as f, open(_HERE / outfile, "w") as j:
        output = []
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            output.append(tuple(line.strip().split(':')))
        json.dump(output, j, indent=2)

def json_passwd(filename):
    output = []
    for one_line in open(filename):
        if one_line.startswith('#'):
            continue
        if one_line.strip().startswith('\n'):
            continue

        output.append(tuple(one_line.split(':')))

    return json.dumps(output, indent=2)



if __name__ == "__main__":
    psswrd_2_json("passwd.txt", "passwd.json")
    # psswrd_2_json_c("passwd.txt", "passwd2.json")
    # print(json_passwd('passwd.txt'))