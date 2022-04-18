class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def preorder(node):  # 전위 순회
    print(node.data, end='') # left,right 노드로 가기전에 print
    if node.left_node != '.':
        preorder(tree[node.left_node])
    if node.right_node != '.':
        preorder(tree[node.right_node])


def inorder(node):  # 중위 순회
    if node.left_node != '.':
        inorder(tree[node.left_node])
    print(node.data, end='') # left에 방문할 것이 없을 때 print
    if node.right_node != '.':
        inorder(tree[node.right_node])


def postorder(node):  # 후위 순회
    if node.left_node != '.':
        postorder(tree[node.left_node])
    if node.right_node != '.':
        postorder(tree[node.right_node])
    print(node.data, end='') # left와 right에 방문할 것이 없을 때


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left_node, right_node = map(str, input().split())
        tree[node] = Node(data=node, left_node=left_node, right_node=right_node)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
    # print(tree)
    # {
    #     'A': <__main__.Node object at 0x100fa6d90>,
    #     'B': <__main__.Node object at 0x100fa6d00>,
    #     'C': <__main__.Node object at 0x100fa6be0>,
    #     'E': <__main__.Node object at 0x100fa6b80>,
    #     'F': <__main__.Node object at 0x100fa6b20>,
    #     'D': <__main__.Node object at 0x100fa6ac0>,
    #     'G': <__main__.Node object at 0x100fa6a60>
    # }
    # print(tree['A'].left_node) # B
    # print(tree['A'].right_node) # C