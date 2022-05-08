import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

visited = [0 for _ in range(n)]
temp = []
answer = []

def dfs(depth):
    if depth == k:
        answer.append("".join(map(str, temp)))
        return
    for i in range(n):
        if not visited[i]:

            visited[i] = 1
            temp.append(cards[i])

            dfs(depth+1)

            temp.pop()
            visited[i] = 0
dfs(0)

print(len(set(answer)))