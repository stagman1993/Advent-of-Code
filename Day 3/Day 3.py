import re

file = "Day 3 input.txt"
file_string = open(file, "r").read()

test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

#Part 1:
m = re.findall(r"mul\((-?\d+),\s*(-?\d+)\)", file_string)

calculated_values = []

for item in m:
    value_1 = int(item[0])
    value_2 = int(item[1])
    calculated_value = value_1 * value_2
    calculated_values.append(calculated_value)

print(sum(calculated_values))

