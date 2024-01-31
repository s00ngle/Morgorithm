import math

N = int(input())

is_prime = [False, False] + [True] * (N - 1) # [False, False, True, True, False, ....]
# is_prime[0] : False
# is_prime[1] : False

# 인덱스가 소수인 것들만 True
for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(2 * i, N + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, N + 1) if is_prime[i]]
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ..., 37, 41]
#                                                        lr
# n = 41
left = 0
right = -1
ans = 0 # 3
s = 0 # 41

while True:
    if s > N:
        s -= primes[left]
        left += 1
    else:
        if s == N:
            ans += 1

        if right + 1 >= len(primes):
            break

        right += 1
        s += primes[right]

print(ans)