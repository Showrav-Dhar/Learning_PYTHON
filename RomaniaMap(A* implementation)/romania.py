import heapq


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):  # to add a tuple (cost, city) to the self.cities , MinHeap Tree
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if not self.cities:
            return True
        else:
            return False

    def check(self):
        print(self.cities)


# takes the heuristics dictionary, returns the straight line distance from a node to bucharest
def heuristic(node, values):
    return values[node]


def astar(start, end, romania, heuristics):
    path = {}  # keeps track of parent of each city
    distance = {}  # keeps track of distance from Arad to each city
    q = priorityQueue()  # to store the f(n) values and city2
    h = heuristics  # copy of heuristics dictionary

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while not q.isEmpty():  # loop will run until q is empty
        current = q.pop()
        expandedList.append(current)

        if current == end:  # Loop Break if we reach the end city
            break

        #   exploring neighbours , new_city = neighbor of current city
        for new_city, new_distance in romania[current]:  # Access city and distance from tuple
            g_cost = distance[current] + new_distance  # g(n) = distance from start node to current node

            if new_city not in distance or g_cost < distance[new_city]:
                distance[new_city] = g_cost
                f_cost = g_cost + heuristic(new_city, h)  # f(n) = g(n) + h(n)
                q.push(new_city, f_cost)  # Add neighbor to queue
                path[new_city] = current  # Update the parent of the neighbor

    finalpath = []
    i = end

    while path.get(i) is not None:  # Backtracking to start node
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("Cities that might be explored : " + str(expandedList))
    print("Number of cities passed through : " + str(len(expandedList)))
    print("Cities passed with the shortest distance : " + str(finalpath))
    print("Number of cities passed through : " + str(len(finalpath)))
    print("Total distance : " + str(distance[end]))


if __name__ == "__main__":
    RomaniaMap = {
        "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118), ],
        "Zerind": [("Arad", 75), ("Oradea", 71), ],
        "Oradea": [("Zerind", 71), ("Sibiu", 151), ],
        "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80), ],
        "Timisoara": [("Arad", 118), ("Lugoj", 111), ],
        "Lugoj": [("Timisoara", 111), ("Mehadia", 70), ],
        "Fagaras": [("Sibiu", 99), ("Bucharest", 211), ],
        "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146), ],
        "Mehadia": [("Lugoj", 70), ("Dobreta", 75), ],
        "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Urziceni", 85), ("Giurglu", 90), ],
        "Pitesti": [("Bucharest", 101), ("Rimnicu Vilcea", 97), ("Craiova", 138), ],
        "Craiova": [("Rimnicu Vilcea", 146), ("Pitesti", 138), ("Dobreta", 120), ],
        "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142), ],
        "Hirsova": [("Urziceni", 98), ("Eforie", 86), ],
        "Vaslui": [("Urziceni", 142), ("Lasi", 92), ],
        "Lasi": [("Vaslui", 92), ("Neamt", 87), ],
        "Dobreta": [("Mehadia", 75), ("Craiova", 120), ],
        "Eforie": [("Hirsova", 86), ],
        "Neamt": [("Lasi", 87), ],
    }

    HeuristicValues = {
        "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242, "Eforie": 161,
        "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Lasi": 226, "Lugoj": 244,
        "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100,
        "Rimnicu Vilcea": 193, "Sibiu": 253, "Timisoara": 329,
        "Urziceni": 80, "Vaslui": 199, "Zerind": 374,
    }

    start = "Arad"
    end = "Bucharest"
    print("\nAfter applying A* algorithm from Arad To Bucharest - \n")
    astar(start, end, RomaniaMap, HeuristicValues)
