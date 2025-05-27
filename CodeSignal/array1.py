def solution(arrayA, arrayB):
    n = len(arrayA)
    visitedA = set()
    result = []
    posA = 0

    while posA not in visitedA:
        visitedA.add(posA)
        posB = arrayA[posA] - 1  
        result.append(posB + 1)
        posA = arrayB[posB] - 1  

    return result

arrayA = [1, 3, 2, 5, 4]
arrayB = [5, 4, 3, 2, 1]
solution(arrayA, arrayB)