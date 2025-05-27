def solution(numbers):
    # TODO: implement the function according to problem statement
    array = []
    for num in numbers:
        if num % 10 == 0:
            num = 1
            array.append(num)
        else:
            num += 1
            array.append(num)
    frecuency = {}
    for i in array:
        if i in frecuency:
            frecuency[i] += 1
        else:
            frecuency[i] = 1
    products = []
    for i, freq in frecuency.items():
        products.append(i * freq)
    products.sort(reverse=False)
    return products
    
    
numbers = [4, 13, -15, 20, 100, -10, -99, 98]
print(solution(numbers))