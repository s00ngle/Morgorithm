import sys
sys.setrecursionlimit(10**5)

prefix_tree = []

while True:
    try:
        prefix_tree.append(int(input()))
    except:
        break

def postorder(s, e):
    if s == e:
        return
    
    mid = e
    for i in range(s + 1, e):
        if prefix_tree[i] > prefix_tree[s]:
            mid = i
            break
    
    postorder(s + 1, mid)
    postorder(mid, e)
    print(prefix_tree[s])

postorder(0, len(prefix_tree))dd