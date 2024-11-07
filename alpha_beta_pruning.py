import math 

def min_max(currentDepth, NodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if(currentDepth == targetDepth):
        return scores[NodeIndex]
    if maxTurn:
        alpha = -math.inf
        leftEval = min_max(currentDepth + 1, NodeIndex * 2, False, scores, targetDepth, alpha, beta)
        maxEval = max(alpha, leftEval)
        alpha = max(alpha, maxEval)
        if alpha >= beta:
            return maxEval
        rightEval = min_max(currentDepth + 1, NodeIndex * 2 + 1, False, scores, targetDepth, alpha, beta)
        maxEval = max(alpha, rightEval)
        alpha = max(alpha, maxEval)
        return maxEval
    else:
        beta = math.inf
        leftEval = min_max(currentDepth + 1, NodeIndex * 2, True, scores, targetDepth, alpha, beta)
        minEval = min(beta, leftEval)
        beta = min(beta, minEval)
        if alpha >= beta:
            return minEval
        rightEval = min_max(currentDepth + 1, NodeIndex * 2 + 1, True, scores, targetDepth, alpha, beta)
        minEval = min(beta, rightEval)
        beta = min(beta, minEval)
        return minEval


scores = [3, 5, 6, 9, 1, 2, 0, -1] 
treeDepth = math.log(len(scores),2)
print("The optimal value is : ",end="")
alpha = -math.inf
beta = math.inf
print(min_max(0,0,True,scores,treeDepth,alpha,beta))