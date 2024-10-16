def length(txt):
    def recursive_len(s, index=0):
        if index == len(s):
            return 0
        else:
            return 1 + recursive_len(s, index + 1)
    
    def format_string(s, index=0):
        if index >= len(s):
            return ''
        else:
            char = s[index]
            if index % 2 == 0:
                return char + '*' + format_string(s, index + 1)
            else:
                return char + '~' + format_string(s, index + 1)
    
    length = recursive_len(txt)
    
    formatted_str = format_string(txt)
    print(formatted_str)
    
    return length

print(length(input("Enter Input : ")))
