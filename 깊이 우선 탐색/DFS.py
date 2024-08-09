from collections import deque
'''
DFS 기본 원칙
데이터를 찾을 때 항상 앞으로 찾아야 할 노드와 이미 방문한 노드를 기준으로 데이터를 탐색한다.

DFS는 스택/큐 또는 재귀함수를 통해 구현할 수 있다.
'''


# 스택(리스트)를 이용한 DFS
def DFS_stack(graph, start_node):
    '''
    스택이 비어있을 때까지 반복한다.
    스택에서 노드를 하나 꺼내고, 결과 리스트에 추가한다.
    꺼낸 노드와 연결된 모든 인접 노드를 순회한다.
    방문하지 않은 인접 노드가 있다면 스탹에 추가하고 방문 처리한다.

    :param graph: 인접 리스트 형태의 그래프
    :param start_node: 시작 노드
    :return: 방문한 노드들의 리스트
    '''
    need_visited, visited = list(), list()

    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)

            need_visited.extend(graph[node])

    return visited


# 재귀를 이용한 DFS
def DFS_recursive(graph, start, visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            DFS_recursive(graph, node, visited)

    return visited


# deque를 이용한 DFS
def DFS_deque(graph, start_node):
    visited = []
    need_visited = deque()

    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited


graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(DFS_stack(graph, 'A'))
print(DFS_recursive(graph, 'A'))
print(DFS_deque(graph, 'A'))
