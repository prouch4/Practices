def solution(strings, numbers):
    # TODO: implement the solution according to the task
    new_string = ''
    sum_num = 0
    i = 0
    
    while i < len(strings) and sum_num <= 100:
        if strings[i] == 'a' or strings[i] == 'e' or strings[i] == 'i' or strings[i] == 'o' or strings[i] == 'u':
            break
        else:
            new_string += 'z' if strings[i] == 'a' else chr(ord(strings[i]) - 1)
            num = abs(numbers[i])*2
            sum_num += num
            i += 1
    return new_string, numbers[i:]

strings = 'abcdef'
numbers = [10, 20, 30, 40, 50, 60]
print(solution(strings, numbers))