with open("input", "r") as tmp_file:
    crabs_pos = [int(i) for i in tmp_file.readline().split(",")]

# part 1
pos_max = max(crabs_pos)
crabs = [crabs_pos.count(i) for i in range(pos_max + 1)]

fuel = [0 for i in range(pos_max + 1)]

for i in range(pos_max + 1):
    for c in range(pos_max + 1):
        fuel[i] += abs(c - i) * crabs[c]

print(min(fuel))

# part 2

fuel = [0 for i in range(pos_max + 1)]

for i in range(pos_max + 1):
    for c in range(pos_max + 1):
        exp = sum(range(0, abs(c - i) + 1))
        fuel[i] += exp * crabs[c]

print(min(fuel))
