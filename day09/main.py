with open("input", "r") as in_file:
    tmp = in_file.read().splitlines()
    heights = [[int(el) for el in row] for row in tmp]

# part 1
def is_low_point(t, x, y):
    lowest = True
    increments = [-1, 0, 1]
    pos_increments = [(x, y) for x in increments for y in increments if (x, y) != (0, 0)]

    for i,j in pos_increments:
        check_col = y + i >= 0 and y + i < len(t)
        check_row = x + j >= 0 and x + j < len(t[0])
        if check_col and check_row:
            if t[y][x] >= t[y + i][x + j]:
                lowest = False
    return lowest

risk_sum = 0

for y in range(len(heights)):
    for x in range(len(heights[0])):
        if is_low_point(heights, x, y):
            risk_sum += 1 + heights[y][x]

print(risk_sum)

# part 2
def is_near(pos, t, x, y):
    pos_increments = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for i, j in pos:
        for h, k in pos_increments:
            if x + h == i and y + k == j:
                pos.append((x, y))
                return True
    return False

basins = []
inserted = []
basin_nums = sum([len(list(filter(lambda x:(x != 9), row))) for row in heights])

for y in range(len(heights)):
    for x in range(len(heights[0])):
        if is_low_point(heights, x, y):
            basins.append([(x, y)])
            inserted.append((x, y))

while len(inserted) < basin_nums:
    for y in range(len(heights)):
        for x in range(len(heights[0])):
            if heights[y][x] != 9 and (x, y) not in inserted:
                for i in range(len(basins)):
                    if is_near(basins[i], heights, x, y):
                        inserted.append((x, y))

basins_len = [len(row) for row in basins]
prod = 1
for i in range(3):
    prod = prod * max(basins_len)
    basins_len.pop(basins_len.index(max(basins_len)))

print(prod)
