import re

def parse_syscalls(path):
    syscalls = []
    with open(path, "r", errors="ignore") as f:
        for line in f:
            m = re.search(r"\b([a-zA-Z_]+)\(", line)
            if m:
                syscalls.append(m.group(1))
    return syscalls
