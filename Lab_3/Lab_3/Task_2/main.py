def canIntroduceAllPeople(N, A):
    graph = {i: [] for i in range(1, N + 1)}

    for i, ai in enumerate(A, start=1):
        if ai > N - 1:
            return False
        for j in range(1, ai + 1):
            if i + j <= N:
                graph[i].append(i + j)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(1)

    return len(visited) == N

N = 5
A = [2, 1, 2, 1, 1]

result = canIntroduceAllPeople(N, A)
print(result)
