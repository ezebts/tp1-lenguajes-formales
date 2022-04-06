
def calculator(input_operation):
    terms = []
    tokens = []
    
    for idx, char in enumerate(input_operation):
        
        if char == ')':
            start = terms.pop()
            sliced = input_operation[start : idx + 1]
            result = eval(sliced)
            tokens.append((result, sliced))
        
        elif char == '(':
            terms.append(idx)
        
    return (tokens[-1][0], tokens[0][1])
