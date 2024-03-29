A = [""] + list(input())
B = [""] + list(input())
LCS = [[""]*len(B) for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1], key = len)

result = LCS[-1][-1]

print(len(result))
print(result)