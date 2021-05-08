## Argparse

import argparse

parser = argparse.ArgumentParser(description="Process file...")
parser.add_argument("-o", '--out_file', type=str)
parser.add_argument("-n", "--names", type=str, nargs="+")
parser.add_argument("-i", "--integers", type=int, nargs="+")

args = parser.parse_args()
print(args)

with open(args.out_file, 'w') as f:
    for n, i in zip(args.names, args.integers):
        f.write(f"{n}, {i ** 2}\n")
