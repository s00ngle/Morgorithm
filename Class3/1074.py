N, r, c = map(int, input().split())

def Z(n, x, y):
    if n == 1:
        return 2 * x + y
    else:
        half = 2 ** (n - 1)
        if x < half and y < half:
            return Z(n - 1, x, y)
        elif x < half and y >= half:
            return half * half + Z(n - 1, x, y - half)
        elif x >= half and y < half:
            return 2 * half * half + Z(n - 1, x - half, y)
        else:
            return 3 * half * half + Z(n - 1, x - half, y - half)
        
print(Z(N, r, c))