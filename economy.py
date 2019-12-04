n = int(input())
price = [[int(p) for p in input().split()] for i in range(n - 1)]
a, b = [int(i) for i in input().split()]
ia = max(a, b) - 1
ja = min(a, b)
a_to_b = price[ia][ja]
current_station = a
for i in range(len(price)):
    for j in range(len(price[i])):
        print(j)

for i in range(n):
    if i not in [a, b]:
        cur_a_i = max(a, i) - 1
        cur_a_j = min(a, i)
        cur_b_i = max(b, i) - 1
        cur_b_j = min(b, i)
        if a_to_b > price[cur_a_i][cur_a_j] + price[cur_b_i][cur_b_j]:
            a_to_b = price[cur_a_i][cur_a_j] + price[cur_b_i][cur_b_j]
            current_station = i
print(current_station)
