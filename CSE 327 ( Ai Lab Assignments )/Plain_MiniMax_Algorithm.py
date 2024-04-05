# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

#   video for visualization - https://youtu.be/l-hh51ncgDI?si=cWhkfwjal4RrAKYO


# maxTurn = false means mini
# maxTurn = True means max
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):  # inorder traversal
    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        leftChild = minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth)
        rightChild = minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        return max(leftChild, rightChild)

    else:
        leftChild = minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth)
        rightChild = minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        return min(leftChild, rightChild)


# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, treeDepth))
