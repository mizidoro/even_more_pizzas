from node import Node


def get_indexes(x, xs): return [i for (
    y, i) in zip(xs, range(len(xs))) if x == y]


def createDeliveryTrees(teams, team_index):
    child = []

    if(team_index == 0):
        for j in range(teams[0], 0, -1):
            node = Node()
            node.data = [j, 2]
            child.append(node)
    else:
        for i in range(team_index, 3):
            team_type = i + 2
            for j in range(teams[i], 0, -1):
                node = Node()
                node.data = [j, team_type]
                child.append(node)

    if(team_index == 2):
        return child

    for c in child:
        index = (c.data[1] - 2) + 1
        if(index >= 1 and index <= 2):
            next_level = createDeliveryTrees(teams, index)
            for nc in next_level:
                c.appendChild(nc)

    return child


def createDeliveryPossibilities(teams, possibilities_by_level):
    for l in range(len(possibilities_by_level), 1, -1):
        for p1 in teams[l-1]:
            nodes = teams[l].copy()
            for p2 in nodes:
                p1.appendChild(p2)


def createDeliveryPossibilitiesByLevel(teams, level):
    child = []

    team_type = level + 2

    for j in range(teams[level], 0, -1):
        node = Node()
        node.data = [j, team_type]
        child.append(node)

    return child


def findTreePaths(root, paths, level):
    for i in range(1, level + 2):

        path = getPath(root, i)

        if (len(get_indexes(path, paths)) == 0):
            paths.append(path)

        for child in root.child:
            findTreePaths(child, paths, level+1)


def getPath(child, depth):
    path = []
    aux = child
    i = 0
    while (aux != None and i < depth):
        path.append(aux.data)
        aux = aux.parent
        i += 1
    return path
