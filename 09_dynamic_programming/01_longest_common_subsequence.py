# Самая длинная общая подстрока
word_a = 'fish'
word_b = 'hish'
cell = []

for i, letter_a in enumerate(word_a):
    cell.append([])
    for j, letter_b in enumerate(word_b):
        cell[i].append(0)

        if word_a[i] == word_b[j]:
            # The letters match.
            cell[i][j] = cell[i - 1][j - 1] + 1
        else:
            # The letters don't match.
            cell[i][j] = 0

print(cell)

# word_a = 'fish'
# word_b = 'fosh'

# word_a = 'fosh'
# word_b = 'fort'

word_a = 'blue'
word_b = 'clues'

cell = []

for i, letter_a in enumerate(word_a):
    cell.append([])
    for j, letter_b in enumerate(word_b):
        cell[i].append(0)

        if word_a[i] == word_b[j]:
            # The letters match.
            cell[i][j] = cell[i - 1][j - 1] + 1
        else:
            # The letters don't match.
            cell[i][j] = max(cell[i - 1][j], cell[i][j - 1])

print(cell)

