# https://www.youtube.com/watch?v=SmOrBW22R2k&t=702s
class Graph:
    def __init__(self, num_nodes, edges):  # constructor
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]  # adjacency list [ list of empty list ]
        for n1, n2 in edges:  # in edges list there are tuples, and we are accessing the two values of each tuple
            self.data[n1].append(n2)  # node1 is connected to node2
            self.data[n2].append(n1)  # node2 is connected to node1

    def __repr__(self):
        return "\n".join(["{}: {}".format(node, neigbours) for node, neigbours in
                          enumerate(self.data)])  # it gives value and indices of the list

    def __str__(self):
        return self.__repr__()

    def add_edge(self, source, destination):
        if source < 0 or source >= self.num_nodes or destination < 0 or destination >= self.num_nodes:
            print("Value Error")
        else:
            self.data[source].append(destination)
            self.data[destination].append(source)

    def remove_edge(self, source, destination):
        if source < 0 or source >= self.num_nodes or destination < 0 or destination >= self.num_nodes:
            print("Value Error")
        else:
            self.data[source].remove(destination)
            self.data[destination].remove(source)

    def BFS(self, root):
        queue = []
        discovered = [False] * len(self.data)
        distance = [None] * len(self.data)
        parent = [None] * len(self.data)

        discovered[root] = True
        queue.append(root)
        distance[root] = 0
        idx = 0  # to keep track of the queue items

        while idx < len(queue):
            # these two line means deque
            current = queue[idx]
            idx += 1

            # check all edges of the current

            for node in self.data[current]:
                if not discovered[node]:  # means discovered[node] = False
                    distance[node] = 1 + distance[current]
                    parent[node] = current
                    discovered[node] = True
                    queue.append(node)

        return queue, distance, parent


if __name__ == '__main__':
    num_nodes = 5
    edges = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 3), (1, 4), (3, 4)]
    graph1 = Graph(num_nodes, edges)
    # for i in range(len(graph1.data)):
    #     print(f"for Node {i} connected nodes are = ", end=' ')
    #     for j in range(len(graph1.data[i])):
    #         print(graph1.data[i][j], end=' ')
    #     print()

    # for x in enumerate([10,30,40,50,60]): # testing what enumerate dose
    #     print(x)
    # print(graph1)  # prints the adjacency list

    # question 1 - Write a function to add an edge to a graph represented as an adjacency list.
    #     graph1.add_edge(0, 3)
    #     print("With New Edge")
    #     print(graph1)

    # question 2 - Write a function to remove an edge from a graph represented as a adjacency list.
    #     graph1.remove_edge(0, 3)
    #     print("With deleted Edge")
    #     print(graph1)

    # Breadth-First-Search
    # question 3 - implement breadth-first search given a source node in a graph using Python.
    root_node = 1
    Que, Dis, parents = graph1.BFS(root_node)
    print("Traversing order")
    print(Que)
    print(f"Distance From rootNode - {root_node}")
    print(Dis)
    print(f"Parents of each node with respect to {root_node}")
    print(parents)

    # question 4 - Write a program to check if all the nodes in a graph are connected
