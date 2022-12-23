def swap_case(s):
    string =[char for char in s]
    
    for indx, char in enumerate(string):
        if char == char.upper():
            string[indx] = char.lower()
        if char == char.lower():
            string[indx] = char.upper()
            
    return "".join(string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)