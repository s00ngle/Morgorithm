n = int(input()) # n = 4

cnt = 0 # cnt = 2
board = [0] * n # [0, 0, 0, 0]

# 열 : 0, 1, 2, 3
# 0 : [0, 1, 0, 0]
# 1 : [0, 0, 0, 1]
# 2 : [1, 0, 0, 0]
# 3 : [0, 0, 1, 0]

#board[1, 0, 0, 0]

# board[x] = y : x번째 열에 y번째 행에 퀸을 놓았다.
# x : 놓을 위치, i : 비교할 위치
def check(x) : # x = 1
    for i in range(x) : # i : 0 ~ x-1
        if board[i] == board[x] or abs(x - i) == abs(board[x] - board[i]) : # 가로 차이 == 세로 차이
            return False
    return True

def Nqueen(x) : # x : 열 번호
    global cnt

    if x == n: # 탈출조건
        cnt += 1
        return

    # x = 0
    for 행번호 in range(n) : # 행번호 : 0 ~ n-1
        board[x] = 행번호
        if check(x) :
            Nqueen(x + 1) # Nqueen(4)

Nqueen(0)

print(cnt)