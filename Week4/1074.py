N, r, c = map(int, input().split())

def Z(n, x, y):
    if n == 1:
        return 2 * x + y
        # 0 : (0, 0), 1 : (0, 1)
        # 2 : (1, 0), 3 : (1, 1)
    else:
        half = 2 ** (n - 1) # 2

        if x < half and y < half: # 왼쪽 위
            return                                  Z(n - 1, x, y)
        elif x < half and y >= half: # 오른쪽 위
            return half * half                                  + Z(n - 1, x, y - half)
        elif x >= half and y < half: # 왼쪽 아래
            return 2 * half * half                                  + Z(n - 1, x - half, y) # (1, 1, 1) : 3
        else: # 오른쪽 아래
            return 3 * half * half                                  + Z(n - 1, x - half, y - half)
                # 3 * 4 * 4 + 3 -> 51
                # Z(2, 1, 1)  -> Z(1, 1, 1) : 3
print(Z(N, r, c)) # 11
# 2, 3, 1


# 31

# 00 01   02 03
# 10 11   12 13

# 20 21   22 23
# 30 31   32 33

#  0  1  4  5
#  2  3  6  7
#  8  9 12 13
# 10 11 14 15