import re

file = "Test Set.txt"

rules = []
reports = []

with open(file, "r") as f:
    data = f.readlines()
    for line in data:
        if re.search(r'\d\d\|\d\d', line):
            split = line[:len(line)-1].split('|')
            numeric = list(map(int, split))
            rules.append(numeric)
        else:
            if line[:len(line)-1] == "":
                continue
            else:
                split = line[:len(line)-1].split(',')
                numeric = list(map(int, split))
                reports.append(numeric)

print(rules)
print(reports)