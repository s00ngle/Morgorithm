L, C = map(int, input().split())
alphabet = list(input().split())

alphabet.sort()

def check(code):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowelCnt = 0

    for i in code:
        if i in vowel:
            vowelCnt += 1

    consonantCnt = L - vowelCnt
    
    return vowelCnt >= 1 and consonantCnt >= 2

# alphabet : ['a', 'c', 'i', 's', 't', 'w']

def DFS(code, index):
    if len(code) == L and check(code):
        print(code)
        return

    for i in range(index, C): # 0 ~ 5
        DFS(code + alphabet[i], i + 1)
        # DFS('a', 1)
            # DFS('ac', 2)
                # DFS('aci', 3)
                    # DFS('acis', 4)
                    # DFS('acit', 4)
                    # DFS('aciw', 4)
                # DFS('acs', 3)

DFS('', 0)