def solution(roadA, roadB):
    route = []
    n = len(roadA)

    for start in range(n):
        posA = start
        visitedA = set()
        visitedB = set()
        jumps = 0

        while posA not in visitedA:
            visitedA.add(posA)

            # Saltar de A→B
            posB = roadA[posA]
            jumps += 1

            # Si B ya lo visitamos, terminamos esta ruta
            if posB in visitedB:
                break
            visitedB.add(posB)

            # Saltar de B→A
            posA = roadB[posB]
            jumps += 1

        route.append(jumps)

    return route