def solution(s):
    s_3 = ''
    ascii_vals = []
    original_chars = []  # Guardamos las letras originales
    
    for letter in s:
        if letter == 'a':
            s_3 += 'x'
            val = 'x'
            original = 'a'
        elif letter == 'b':
            s_3 += 'y'
            val = 'y'
            original = 'b'
        elif letter == 'c':
            s_3 += 'z'
            val = 'z'
            original = 'c'
        else:
            s_3 += chr(ord(letter) - 3)
            val = chr(ord(letter) - 3)
            original = letter
    
        ascii_vals.append(val)
        original_chars.append(original)
    
    frecuency = {}
    result = {}  # Nuevo diccionario para el resultado
    
    for i in range(len(ascii_vals)):
        if ascii_vals[i] in frecuency:
            frecuency[ascii_vals[i]] += 1
        else:
            frecuency[ascii_vals[i]] = 1
            
    for i, freq in frecuency.items():
        # Encontramos el índice de la letra transformada
        idx = ascii_vals.index(i)
        # Usamos la letra original correspondiente
        result[original_chars[idx]] = freq * ord(i)

    return result
    
    
    
    
s = 'abc'
print(solution(s))