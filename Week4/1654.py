k, n = map(int, input().split())

lans = []

for _ in range(k):
    lans.append(int(input()))

left = 1
right = max(lans)
ans = 0 # 11

# 4 11

# 802
# 743
# 457
# 539

# left : 200, right : 200
while left <= right:

    mid = (left + right) // 2 # mid : 200

    lens_div = [x // mid for x in lans] # [4, 3, 2, 2]
    count = sum(lens_div)

    # left ~ right
    if count >= n:
        ans = mid
        left = mid + 1
    if count < n:
        right = mid - 1

print(ans)