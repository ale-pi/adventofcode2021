def is_h_or_v(line):
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return True
    return False

with open("input", "r") as tmp_file:
    tmp = tmp_file.read().splitlines()
    lines = [[[int(c) for c in p.split(",")] for p in line.split(" -> ")] for line in tmp]

x_max = max(map(lambda x:(max(x[0][0], x[1][0])), lines))
y_max = max(map(lambda x:(max(x[0][1], x[1][1])), lines))
seabed = [[0 for i in range(y_max + 1)] for j in range(x_max + 1)]

# part 1
lines_hv = list(filter(is_h_or_v, lines))
for line in lines_hv:
    if line[0][0] == line[1][0]:
        x = line[0][0]
        coords = sorted([line[0][1], line[1][1]])
        for y in range(coords[0], coords[1] + 1):
            seabed[x][y] += 1
    else:
        y = line[0][1]
        coords = sorted([line[0][0], line[1][0]])
        for x in range(coords[0], coords[1] + 1):
            seabed[x][y] += 1

overlapped = sum([len(list(filter(lambda x:(x>1), line))) for line in seabed])
print(overlapped)

# part 2
lines_d = list(filter(lambda x:(not(is_h_or_v(x))), lines))
for line in lines_d:
    x_0 = min(line[0][0], line[1][0])
    x_1 = max(line[0][0], line[1][0])
    if x_0 in line[0]:
        y_0 = line[0][1]
        y_1 = line[1][1]
    else:
        y_0 = line[1][1]
        y_1 = line[0][1]
    m = int((y_0 - y_1)/(x_0 - x_1))
    delta = (x_1 - x_0)
    for i in range(delta + 1):
        seabed[x_0 + i][y_0 + m * i] += 1

overlapped = sum([len(list(filter(lambda x:(x>1), line))) for line in seabed])
print(overlapped)
