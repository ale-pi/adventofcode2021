def split_table(t, d, n):
    if d == "y":
        t1 = t[:n]
        tmp = t[n + 1:]
        t2 = tmp[::-1]
    elif d == "x":
        t1 = [line[:n] for line in t]
        tmp = [line[n + 1:] for line in t]
        t2 = list(map(lambda x:(x[::-1]), tmp))
    return t1, t2

def join_h(t1, t2):
    while len(t1) != len(t2):
        if len(t1) < len(t2):
            t1.insert(0, [0 for i in range(len(t2[0]))])
        else:
            t2.insert(0, [0 for i in range(len(t1[0]))])
    for y in range(len(t2)):
        for x in range(len(t2[0])):
            t1[y][x] += t2[y][x]
    return t1

def join_v(t1, t2):
    while len(t1[0]) != len(t2[0]):
        if len(t1) > len(t2):
            for i in range(len(t1)):
                t1[i].append(0)
        else:
            for i in range(len(t2)):
                t2[i].append(0)
    for y in range(len(t2)):
        for x in range(len(t2[0])):
            t1[y][x] += t2[y][x]
    return t1

def join_tables(t1, t2, d):
    if d == "y":
        t = join_h(t1, t2)
    elif d == "x":
        t = join_v(t1, t2)
    return t

def print_table(t):
    print()
    for line in t:
        for el in line:
            if el > 0:
                print("█", end="")
            else:
                print(" ", end="")
        print()

with open("input", "r") as data_file:
    data = [d.splitlines() for d in data_file.read().split("\n\n")]
    dots = [[int(c) for c in line.split(",")] for line in data[0]]
    tmp = [line.rsplit(" ", 1)[1].split("=") for line in data[1]]
    fold = [[a, int(b)] for a, b in tmp]

x_len = max(map(lambda x: x[0], dots))
y_len = max(map(lambda x: x[1], dots))

paper = [[0 for x in range(x_len + 1)] for y in range(y_len + 1)]
for x, y in dots:
    paper[y][x] = 1

# part 1
t1, t2 = split_table(paper, fold[0][0], fold[0][1])
paper = join_tables(t1, t2, fold[0][0])
fold.pop(0)

n_dots = sum([len(list(filter(lambda x:(x > 0), line))) for line in paper])
print(n_dots)

# part 2
for d, n in fold:
    t1, t2 = split_table(paper, d, n)
    paper = join_tables(t1, t2, d)

print_table(paper)
