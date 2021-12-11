# return the number of elements of a list that are larger than the previous one
def larger_than_previous(l):
    cont = 0
    for i in range(len(l) - 1):
        if l[i+1] - l[i] > 0:
            cont += 1
    return cont

# part 1
tmp = open("input", "r")
depths = [int(i) for i in tmp.readlines()]
tmp.close()
print(larger_than_previous(depths))

# part 2
depths_sum = [sum(depths[i:i+3]) for i in range(len(depths) - 2)]
print(larger_than_previous(depths_sum))
