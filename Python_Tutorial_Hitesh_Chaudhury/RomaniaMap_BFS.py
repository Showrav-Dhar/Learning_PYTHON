# we need queue to perform bfs
from queue import Queue

romaniaMap = {
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


def GreedyBFS(StartingNode, DestinationNode):
    visited = {}  # for keeping track of the visited nodes, dictionary
    distance = {}  # keeping track of the distance , dictionary
    # Distance means how far it is from the starting node,
    # and prioritize exploring closer neighbors, ultimately leading to the discovery of the shortest path.
    parent = {}  # keeping track of the parents of a node, dictionary

    BFS_result = []  # list
    queue = Queue()  # to maintain the order of traversal

    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1
    # initially no city is visited to everything is set to false

    startingCity = StartingNode
    visited[startingCity] = True
    distance[startingCity] = 0  # because startingCity is in the top of the tree
    queue.put(startingCity)  # put(item) – Put an item into the queue.

    while not queue.empty():  # loop will continue until queue is empty
        u = queue.get()  # get() – Remove and return an item from the queue.
        BFS_result.append(u)  # stores the nodes, by the order they are visited

        # explore the adjacent nodes of u
        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u  # the parent of v is u
                # distance[v] = distance[u] + 1  # means how far it is from the starting node.level - 1,2,3...
                queue.put(v)

    g = DestinationNode
    path = []  # start to destination
    while g is not None:
        path.append(g)
        g = parent[g]  # we are going backward from destination to start,
        # so when g = arad , it will be None , because arad has no parent
        # then the loop will stop

    path.reverse()  # to show the path from start ot end
    print(path)


if __name__ == '__main__':
    StartNode = 'Arad'
    DestinationNode = 'Bucharest'
    GreedyBFS(StartNode, DestinationNode)
