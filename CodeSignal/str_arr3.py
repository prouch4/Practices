def solution(arr, text):
    # TODO: implement
    new_string = ''
    sum_num = 0
    i = 0
    
    while i < len(text) and sum_num <= 30 and i < len(arr):
        sum_num += abs(arr[i] - 3)
        if sum_num > 30:
            break
        if text[i] == 'z':
            new_string += 'a'
        elif text[i] == 'Z':
            new_string += 'A'
        elif text[i] == ' ':
            new_string += ' '
        else:
            new_string += chr(ord(text[i]) + 1)
        i += 1

    return new_string, arr[i:]

arr = [2,3,5,7,11,13,17,19,23,29]
text = 'the quick brown fox jumps over the lazy dog'
print(solution(arr, text))
