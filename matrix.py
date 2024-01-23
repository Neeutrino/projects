n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

sum_top = 0
sum_right = 0
sum_bottom = 0
sum_left = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if j > i < n-1-j:
            sum_top += matrix[i][j]
        elif j > i > n-1-j:
            sum_right += matrix[i][j]
        elif j < i > n-1-j:
            sum_bottom += matrix[i][j]
        elif j < i < n-1-j:
            sum_left += matrix[i][j]

print(f'''
Верхняя четверть: {sum_top}
Правая четверть: {sum_right}
Нижняя четверть: {sum_bottom}
Левая четверть: {sum_left}
''')
