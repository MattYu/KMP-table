def kmp_table(pattern):
    length = len(pattern)
    result = [None]*length
    result[0] = 0
    
    i = 1
    j = 0
    while i < length:
        if pattern[i] == pattern[j]:
            result[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                result[i] = 0
                i += 1
            else:
                j = result[j-1]
            
    return result
