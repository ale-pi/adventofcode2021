tmp = open("input", "r")
movements = [[i.split()[0], int(i.split()[1])] for i in tmp.readlines()]
tmp.close()

# part 1
x = y = 0

for m in movements:
    if m[0] == "up":
        y -= m[1]
    elif m[0] == "down":
        y += m[1]
    elif m[0] == "forward":
        x += m[1]

print(x * y)

# part 2
x = y = aim = 0

for m in movements:
    if m[0] == "up":
        aim -= m[1]
    elif m[0] == "down":
        aim += m[1]
    elif m[0] == "forward":
        x += m[1]
        y += aim * m[1]

print(x * y)
