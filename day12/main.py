def check_little_caves(m, p):
    if m == m.lower() and m in p:
        return False
    return True

def check_little_caves_twice(m, p):
    lower_case = list(filter(lambda x:(x == x.lower()), p))
    occ = [lower_case.count(i) for i in lower_case]
    if 2 in occ and m in lower_case:
        return False
    return True

with open("input", "r") as in_file:
    tmp = in_file.read().splitlines()
    connections = [line.split("-") for line in tmp]

starts = list(filter(lambda x:("start" in x), connections))
starts = list(map(lambda x:(["start", x[abs(x.index("start") - 1)]]), starts))

ends = list(filter(lambda x:("end" in x), connections))
ends = list(map(lambda x:([x[abs(x.index("end") - 1)], "end"]), ends))

moves = list(filter(lambda x:("end" not in x and "start" not in x), connections))
moves = moves + list(map(lambda x:([x[1], x[0]]), moves))

# part 1

paths = []
tmp_paths = starts.copy()

while len(tmp_paths) != 0:
    n_paths = len(tmp_paths)
    for i in range(n_paths):
        for m in moves:
            if m[0] == tmp_paths[i][-1] and check_little_caves(m[1], tmp_paths[i]):
                tmp_paths.append(tmp_paths[i] + [m[1]])
        for e in ends:
            if e[0] == tmp_paths[i][-1]:
                paths.append(tmp_paths[i] + [e[1]])
    tmp_paths = tmp_paths[n_paths:]

print(len(paths))

# part 2

paths = []
tmp_paths = starts.copy()

while len(tmp_paths) != 0:
    n_paths = len(tmp_paths)
    for i in range(n_paths):
        for m in moves:
            if m[0] == tmp_paths[i][-1] and check_little_caves_twice(m[1], tmp_paths[i]):
                tmp_paths.append(tmp_paths[i] + [m[1]])
        for e in ends:
            if e[0] == tmp_paths[i][-1]:
                paths.append(tmp_paths[i] + [e[1]])
    tmp_paths = tmp_paths[n_paths:]

print(len(paths))
