def solution(arrayA, arrayB, arrayC):
    visitedA = set()
    posA = 0
    maxB = 0
    maxC = 0
    n = len(arrayA)

    # Recorremos mientras no repitamos posA y esté en rango
    while posA not in visitedA and 0 <= posA < n:
        visitedA.add(posA)

        # —— Fase A → B ——
        posB = arrayA[posA]
        # si el puntero sale de rango, terminamos
        if posB < 0 or posB >= len(arrayB):
            break
        valB = arrayB[posB]
        # actualizamos máximo de B
        if valB > maxB:
            maxB = valB
        # avanzamos posA al valor sacado de B
        posA = valB

        # —— Fase A → C ——
        # comprobamos de nuevo rango de posA en A
        if posA < 0 or posA >= n:
            break
        posC = arrayA[posA]
        if posC < 0 or posC >= len(arrayC):
            break
        valC = arrayC[posC]
        # actualizamos máximo de C
        if valC > maxC:
            maxC = valC
        # avanzamos posA al valor sacado de C
        posA = valC

    print(maxB)  # para depurar: imprime el máximo encontrado en B
    print(maxC)  # para depurar: imprime el máximo encontrado en C
    return maxB + maxC


arrayA = [2, 0, 1]
arrayB = [1, 3, 2]
arrayC = [2, 0, 1]
solution(arrayA, arrayB, arrayC)