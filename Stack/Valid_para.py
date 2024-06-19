def isValid(string):
    bracketMapping = {"(":")", "{":"}", "[":"]"}
    openParams = ["(", "{", "[" ]

    stack = []

    for s in string:
        if s in openParams:
            stack.append(s)
        elif stack and s == bracketMapping[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []


#drivercode
string = "({[]})"
if isValid(string):
    print("This is Valid")
else:
    print("This is Invalid")
