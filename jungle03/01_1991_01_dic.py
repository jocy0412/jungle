from sys import stdin
input = stdin.readline
N = int(input())
tree = {}

for _ in range(N) :
    root, left, right = input().rstrip().split()
    tree[root] = (left,right)
def preorder(root) : # 전위 순회
    if root != "." :
        print(root, end="") # left,right 노드로 가기전에 print
        preorder(tree[root][0])
        preorder(tree[root][1])
def inorder(root) : # 중위 순회
    if root != "." :
        inorder(tree[root][0])
        print(root, end="") # left에 방문할 것이 없을 때 print
        inorder(tree[root][1])
def postorder(root) : # 후위 순회
    if root != "." :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="") # left와 right에 방문할 것이 없을 때

preorder("A")
print()
inorder("A")
print()
postorder("A")

# print(tree)
# {
#     'A': ('B', 'C'),
#     'B': ('D', '.'),
#     'C': ('E', 'F'),
#     'E': ('.', '.'),
#     'F': ('.', 'G'),
#     'D': ('.', '.'),
#     'G': ('.', '.')
# }