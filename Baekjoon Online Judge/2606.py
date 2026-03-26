import sys
input = sys.stdin.readline

def dfs(node):
    global count
    visited[node] = True # 방문 완료
    for next_node in graph[node]:
        if not visited[next_node]: # 방문하지 않은 경우
            count += 1
            dfs(next_node)
    return count

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    count = 0 # 감염된 컴퓨터 수

    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1) # n + 1

    for _ in range(m): # 간선 개수만큼
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = dfs(1) # 시작점, 1번 노드에서 연결된 모든 노드 검색
    print(result)

