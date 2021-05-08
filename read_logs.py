import argparse
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-o", "--outfile")
args = parser.parse_args()


f_name = args.file

user_last_login = {}
user_total_time = defaultdict(int)

with open(f_name) as f:
    for line in f:
        login, action, time = line.strip().split(";")
        if action == "LOGIN":
            user_last_login[login] = int(time)
        else:
            user_total_time[login] += int(time) - user_last_login[login]

if args.outfile:
    with open(args.outfile, 'w') as f:
        f.write("Czas przebywania w systemie:\n")
        for line in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
            f.write(f"- {line[0]}: {line[1]} s\n")
else:
    print("Czas przebywania w systemie: ")
    for line in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
        print(f"- {line[0]}: {line[1]} s")