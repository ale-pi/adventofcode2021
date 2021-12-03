def count_ones(l, pos):
    return sum([int(row[pos]) for row in l])

def most_common(l, pos):
    ones = count_ones(l, pos)
    return int(ones >= len(l) / 2)

def less_common(l, pos):
    ones = count_ones(l, pos)
    return int(ones < len(l) / 2)

with open("input", "r") as report_file:
    report = [i.rstrip("\n") for i in report_file.readlines()]

# part 1
gamma = epsilon = ""

for i in range(len(report[0])):
    n_common = most_common(report, i)
    n_uncommon = less_common(report, i)
    gamma = gamma + str(n_common)
    epsilon = epsilon + str(n_uncommon)

print(int(gamma, 2) * int(epsilon, 2))

# part 2
report_o = report.copy()
report_c = report.copy()

for i in range(len(report[0])):
    if len(report_o) != 1:
        n_o = most_common(report_o, i)
        report_tmp = [j for j in report_o if int(j[i]) == n_o]
        report_o = report_tmp.copy()
    if len(report_c) != 1:
        n_c = less_common(report_c, i)
        report_tmp = [j for j in report_c if int(j[i]) == n_c]
        report_c = report_tmp.copy()

o = int(report_o[0], 2)
c = int(report_c[0], 2)

print(o * c)
