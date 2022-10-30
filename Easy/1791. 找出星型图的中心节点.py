
def findCenter(edges):
    i, j = edges[0][0], edges[0][1]
    for k in range(1, len(edges)):
        if i not in edges[k]: return j
        if j not in edges[k]: return i