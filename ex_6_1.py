import sys

file_name = sys.argv[1]

with open(file_name) as f:
    for i, line in enumerate(f, start=1):
        print(f"{i:3} {line[:-1]}")