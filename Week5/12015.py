import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
LIS = [0]

for num in num_list:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        left = 0
        right = len(LIS)

        while left < right:
            mid = (right + left) // 2
            if LIS[mid] < num:
                left = mid + 1
            else:
                right = mid
        LIS[right] = num

    print(LIS)

print(len(LIS) - 1)

# 9
# 100 200 300 10 20 10 30 20 50

# [0]
# [0, 100]
# [0, 100, 200]
# [0, 100, 200, 300]

# [0, 10, 200, 300]
# [0, 10, 20, 300]
# [0, 10, 20, 300]
# [0, 10, 20, 30]

# [0, 10, 20, 30]
# [0, 10, 20, 30, 50]