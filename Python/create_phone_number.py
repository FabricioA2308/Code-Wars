# https://www.codewars.com/kata/525f50e3b73515a6db000b83/javascript

def create_phone_number(n):
    prefix = ''
    strNumber = ''
    n.insert(6, "-")

    for value in n:
        if(len(prefix) < 3):
            prefix += str(value)
        else:
            strNumber += str(value)

    
    return f"({prefix}) {strNumber}"

# Expected result: (123) 456-7890
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
