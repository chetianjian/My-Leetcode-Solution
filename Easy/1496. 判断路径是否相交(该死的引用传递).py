def isPathCrossing(path):
    direction = {"E": (0, 1), "W": (0, -1), "N":(1, 1), "S": (1, -1)}
    location = [0, 0]
    locationLst = [[0, 0]]

    for i in range(len(path)):
        nextLocation = [location[0], location[1]]
        nextLocation[direction.get(path[i])[0]] = \
            nextLocation[direction.get(path[i])[0]] + direction.get(path[i])[1]
        if nextLocation in locationLst:
            return True
        else:
            locationLst.append(nextLocation)
            location = locationLst[-1]
    return False

print(isPathCrossing(path = "NESWW"))