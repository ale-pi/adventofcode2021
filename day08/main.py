with open("input", "r") as tmp_file:
    data = tmp_file.read().splitlines()
    data_tmp = [row.rsplit(" | ") for row in data]
    patterns = [row[0]. split(" ") for row in data_tmp]
    digits = [row[1].split(" ") for row in data_tmp]

# part 1
cont = 0

for row in digits:
    for el in row:
        if str(len(el)) in "2437":
            cont += 1

print(cont)

# part 2
def find_l6(l, d):
    check = d[4].replace(d[1][0], "").replace(d[1][1], "")
    for el in l:
        if d[1][0] not in el or d[1][1] not in el:
            d[6] = el
        elif check[0] in el and check[1] in el:
            d[9] = el
        else:
            d[0] = el

def find_l5(l, d):
    check = d[4].replace(d[1][0], "").replace(d[1][1], "")
    for el in l:
        if d[1][0] in el and d[1][1] in el:
            d[3] = el
        elif check[0] in el and check[1] in el:
            d[5] = el
        else:
            d[2] = el
    

def trans_digits(row):
    d = ["" for i in range(10)]

    l5 = []
    l6 = []

    for el in row:
        if len(el) == 2:
            d[1] = el
        elif len(el) == 3:
            d[7] = el
        elif len(el) == 4:
            d[4] = el
        elif len(el) == 7:
            d[8] = el
        elif len(el) == 5:
            l5.append(el)
        elif len(el) == 6:
            l6.append(el)

    find_l5(l5, d)
    find_l6(l6, d)
    return d

def compare_digits(d, v):
    if sorted(d) == sorted(v):
        return True
    else:
        return False

total = 0

for i in range(len(patterns)):
    values = trans_digits(patterns[i])
    num = ""
    for digit in digits[i]:
        for j in range(10):
            if compare_digits(digit, values[j]):
                num = num + str(j)
    total += int(num)

print(total)
