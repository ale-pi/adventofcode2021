with open("input", "r") as report_file:
    report = [i.rstrip("\n") for i in report_file.readlines()]

# part 1
gamma = epsilon = ""

for i in range(len(report[0])):
    ones = sum([int(n[i]) for n in report])
    n_common = int(ones >= len(report) / 2)
    n_uncommon = int(ones < len(report) / 2)
    gamma = gamma + str(n_common)
    epsilon = epsilon + str(n_uncommon)

print(int(gamma, 2) * int(epsilon, 2))

# part 2
report_o = report.copy()
report_c = report.copy()

for i in range(len(report[0])):
    if len(report_o) != 1:
        ones_o = sum([int(n[i]) for n in report_o])
        n_o = int(ones_o >= len(report_o) / 2)
        report_tmp = [j for j in report_o if int(j[i]) == n_o]
        report_o = report_tmp.copy()
    if len(report_c) != 1:
        ones_c = sum([int(n[i]) for n in report_c])
        n_c = int(ones_c < len(report_c) / 2)
        report_tmp = [j for j in report_c if int(j[i]) == n_c]
        report_c = report_tmp.copy()

o = int(report_o[0], 2)
c = int(report_c[0], 2)

print(o * c)
