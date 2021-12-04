with open("input", "r") as tmp_file:
    draws = [int(i) for i in tmp_file.readline().split(",")]
    tmp = tmp_file.read().strip("\n").split("\n\n")
    boards = [[[int(i) for i in line.split()] for line in b.split("\n")] for b in tmp]

def mark_number(t, n):
    for line in t:
        if n in line:
            line[line.index(n)] = -1
    return t

def check_win(t):
    for line in t:
        if sum(line) == -len(line):
            return True
    for j in range(len(t)):
        if sum([t[i][j] for i in range(len(t))]) == -len(t):
            return True
    return False

def score(t, n):
    unmarked_sum = 0
    for line in t:
        for el in line:
            if el != -1:
                unmarked_sum += el
    return unmarked_sum * n

# part 1
boards_p1 = boards.copy()
for d in draws:
    boards_p1 = list(map(mark_number, boards_p1, [d]*len(boards_p1)))
    winner = list(filter(check_win, boards_p1))
    if len(winner) != 0:
        break

print(score(winner[0], d))

# part 2
boards_p2 = boards.copy()
not_winner = []
for d in draws:
    boards_p2 = list(map(mark_number, boards_p2, [d]*len(boards_p2)))
    not_winner = list(filter(lambda x:(not(check_win(x))), boards_p2))
    if len(not_winner) == 1:
        loser = not_winner[0]
    elif len(not_winner) == 0:
        break

print(score(loser, d))
