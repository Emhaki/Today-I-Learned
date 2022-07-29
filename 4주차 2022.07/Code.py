a, b, c = map(int, input().split())

result = [a, b, c]
cnt = 0
for i in range(1, 7):
    if result.count(i) == 1:
        cnt += 1
    elif result.count(i) == 2:
        cnt += 2
    elif result.count(i) == 3:
        cnt += 3

if cnt == 1:
    print(10000+f'{a}'*1000)
elif cnt == 2:
    print(1000+f'{result}'*1000)
elif cnt == 3:
    print(max(f'{result}')*100)
