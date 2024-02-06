import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    
    root = postorder[postEnd]
    print(root, end = " ")
    
    leftNode = inorder_index[root] - inStart
    rightNode = inEnd - inorder_index[root]
    
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

preorder(0, n - 1, 0, n - 1)