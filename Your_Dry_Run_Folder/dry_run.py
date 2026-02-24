jewels,stones = input(),input()
c = 0
chk,pattern = [jewels[_]for _ in range(len(jewels))],[stones[x]for x in range(len(stones))]
for _ in chk:
    c = c + pattern.count(_)
print(c)