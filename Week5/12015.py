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

print(len(LIS) - 1)