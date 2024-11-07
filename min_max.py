import math
def min_max(currentDepth, NodeIndex, maxTurn, scores, targetDepth):
    if(currentDepth == targetDepth):
        return scores[NodeIndex]
    if maxTurn:
        return max(min_max(currentDepth + 1, NodeIndex * 2,  False, scores, targetDepth), min_max(currentDepth + 1, NodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(min_max(currentDepth + 1, NodeIndex * 2,  True, scores, targetDepth), min_max(currentDepth + 1, NodeIndex * 2 + 1, True, scores, targetDepth))

scores = [3, 5, 2, 9, 12, 13, 11, 23, 4, 15, 1, 7, 10, 17, 12, 28]
treeDepth = math.log(len(scores),2)
print("The optimal value is : ",end="")
print(min_max(0,0,True,scores,treeDepth))