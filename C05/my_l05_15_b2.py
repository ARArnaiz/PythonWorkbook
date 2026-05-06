import json

def code_ip_address(filename: str) -> dict:
    output = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().split()
            ip = line[0]
            code = line[8]
            output[code] = output.get(code, []) + [ip]
    return output

print(json.dumps(code_ip_address("../apache_log_Gemini.txt"), indent=4))
print(json.dumps(code_ip_address("../apache_log_chatgpt.txt"), indent=4))
print(json.dumps(code_ip_address("../apache_log_DeepSeek.txt"), indent=4))
