def increase_level(l):
    for y in range(len(l)):
        for x in range(len(l[0])):
            l[y][x] += 1

def flash(l, cont):
    go_on = False
    pos = [(x, y) for x in range(-1, 2) for y in range (-1, 2) if (x, y) != (0, 0)]
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] > 9:
                l[y][x] = 0
                cont += 1
                for i,j in pos:
                    check_x = x + i >= 0 and x + i < len(l[0])
                    check_y = y + j >= 0 and y + j < len(l)
                    if check_x and check_y:
                        if l[y + j][x + i] != 0:
                            l[y + j][x + i] += 1
                        if l[y + j][x + i] > 9:
                            go_on = True
    return go_on, cont

# part 1
with open("input", "r") as in_file:
    tmp = in_file.read().splitlines()
    octo = [[int(el) for el in line] for line in tmp]

flash_cont = 0

for step in range(100):
    increase_level(octo)
    flash_again = True
    while flash_again:
        flash_again, flash_cont = flash(octo, flash_cont)

print(flash_cont)

# part 2
with open("input", "r") as in_file:
    tmp = in_file.read().splitlines()
    octo = [[int(el) for el in line] for line in tmp]

steps = 0
octo_sum = 1

while octo_sum != 0:
    increase_level(octo)
    flash_again = True
    while flash_again:
        flash_again = flash(octo, 0)[0]
    steps += 1
    octo_sum = sum(map(lambda x: sum(x), octo))

print(steps)
