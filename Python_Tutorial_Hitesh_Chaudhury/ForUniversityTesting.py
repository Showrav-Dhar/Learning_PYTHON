from queue import Queue


def GreedyBFS(romaniaMap, StartingNode, DestinationNode):
    visited = {}    # for keeping track of the visited nodes,
    distance = {}   # keeping track of the level from root node
    parent = {}     # keeping track of the parents of a node

    BFS_result = []     # result of level order traversal
    queue = Queue()     # to maintain level order traversal

    for city in romaniaMap.keys():
        visited[city] = False   # initially making every city unvisited
        distance[city] = -1     # initially making every city level = -1
        parent[city] = None     # initially making every city with no parent

    StartingCity = StartingNode
    visited[StartingCity] = True    # Marked the starting city visited
    distance[StartingCity] = 0      # root node level = 0
    queue.put(StartingCity)         # start of bfs queue

    while not queue.empty():
        CurrentCity = queue.get()     # taking out the first item of the queue
        BFS_result.append(CurrentCity)

        # visiting adjacent nodes of CurrentCity
        for Neighbour in romaniaMap[CurrentCity]:
            if not visited[Neighbour]:
                visited[Neighbour] = True
                parent[Neighbour] = CurrentCity
                distance[Neighbour] = distance[CurrentCity] + 1
                queue.put(Neighbour)

    g = DestinationNode
    finalResult = []
    while g is not None:    # g will be None for the starting city
        finalResult.append(g)   # going backwards
        g = parent[g]

    finalResult.reverse()
    print(finalResult)


if __name__ == '__main__':
    RomaniaMap = {
        'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
        'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Iasi', 'Urziceni'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }
    StartNode = 'Arad'
    EndNode = 'Bucharest'
    print(f"After Applying BFS on Romania Map , Path from {StartNode} to {EndNode} - ")
    GreedyBFS(RomaniaMap, StartNode, EndNode)




