def remove_pairs(s):
    pair = ["()", "[]", "{}", "<>"]
    removed = True
    while removed:
        old_s = s
        for p in pair:
            while p in s:
                s = s.replace(p, "")
        if old_s == s:
            removed = False
    return s

def is_corrupted(s):
    chunks = [")", "]", "}", ">"]
    pos = []
    for c in chunks:
        if c in s:
            pos.append(s.index(c))
        else:
            pos.append(len(s))
    c_index = min(pos)
    if c_index == len(s):
        return ""
    else:
        return chunks[pos.index(c_index)]

def compl_score(chunk):
    table = chunk.maketrans("([{<", "1234")
    values = chunk.translate(table)
    values = values[::-1]
    score = 0
    for v in values:
        score = score * 5 + int(v)
    return score

with open("input", "r") as in_file:
    code = in_file.read().splitlines()

# part 1
tmp = list(map(remove_pairs, code))
corrupted = list(map(is_corrupted, tmp))

print(corrupted.count(")") * 3 + corrupted.count("]") * 57 + corrupted.count("}") * 1197 + corrupted.count(">") * 25137)

# part 2
incomplete = [tmp[i] for i in range(len(tmp)) if corrupted[i] == ""]

scores = list(map(compl_score, incomplete))
scores.sort()

print(scores[len(scores) // 2])
