def solution(inputString, numbers):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # TODO: implement the solution based on the provided task description
    new_string = ''
    sum_num = 0
    i = 0
    
    while i < len(inputString) and sum_num <= 100 and i < len(numbers):
        char = inputString[i]
        if char in vowels:
            # Encontramos el índice de la vocal actual
            idx = vowels.index(char)
            # Tomamos la vocal siguiente (o la primera si es la última)
            new_string += vowels[idx + 1] if idx < len(vowels) - 1 else vowels[0]
        elif char in consonants:
            # Encontramos el índice de la consonante actual
            idx = consonants.index(char)
            # Tomamos la consonante siguiente (o la primera si es la última)
            new_string += consonants[idx + 1] if idx < len(consonants) - 1 else consonants[0]
        sum_num += numbers[i] * 3
        i += 1
        
    return new_string, numbers[i:]

inputString = 'abcdefghijk'
numbers = [5, 10]
print(solution(inputString, numbers))