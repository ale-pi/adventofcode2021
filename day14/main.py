with open("input", "r") as in_file:
    p0 = in_file.readline().strip("\n")
    data = [line.split(" -> ") for line in in_file.read().strip("\n").splitlines()]
    rules = {line[0]:line[1] for line in data}

# part 1
polymer = p0

for n in range(10):
    i = 0
    while i != len(polymer) - 1:
        pair = polymer[i:i+2]
        ins = rules[pair]
        polymer = polymer[0:i + 1] + ins + polymer[i+1:]
        i += 2

elements = {el:polymer.count(el) for el in polymer}
print(max(elements.values()) - min(elements.values()))

# part 2
polymer = p0
pairs = {r:0 for r in rules}

for i in range(len(polymer) - 1):
    pair = polymer[i:i+2]
    pairs[pair] += 1

for i in range(40):
    incr = {r:0 for r in rules}
    for key in pairs:
        if pairs[key] > 0:
            p1 = key[0] + rules[key]
            p2 = rules[key] + key[-1]
            incr[p1] += pairs[key]
            incr[p2] += pairs[key]
            pairs[key] = 0
    for key in pairs:
        pairs[key] += incr[key]

elements = {el:0 for el in elements}
elements[polymer[0]] = 1/2
elements[polymer[-1]] = 1/2

for key in pairs:
    for el in key:
        elements[el] += pairs[key] / 2

print(int(max(elements.values()) - min(elements.values())))
