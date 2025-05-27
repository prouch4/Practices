def solution(sentence):
    # TODO: Implement the solution following the task description
    new_sentence = ''
    ascii_vals = []
    for character in sentence:
        if character.isalnum():
            if character.isdigit():
                if character == '0':
                    new_sentence += '9'
                    val = '9'
                else:
                    new_sentence += str(int(character) - 1)
                    val = str(int(character) - 1)
            else:
                if character == 'a':
                    new_sentence += 'z'
                    val = 'z'
                elif character == 'A':
                    new_sentence += 'Z'
                    val = 'Z'
                else:
                    new_sentence += chr(ord(character) - 1)
                    val = chr(ord(character) - 1)
        else:
            pass
        ascii_vals.append(val)
    
    frecuency = {}
    for new_char in new_sentence:
        if new_char in frecuency:
            frecuency[new_char] += 1
        else:
            frecuency[new_char] = 1
    
    result = []
    for new_char, freq in frecuency.items():
        result.append(ord(new_char) - freq)
    result.sort()
    return result

sentence = "When in the course of human events..."
print(solution(sentence))