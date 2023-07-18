 

def isValidParenthesis(expression):

    stack = []
    dict = {")": "(", "}": "{", "]": "["}
    for char in expression:
        if char in dict:
            top_element = stack.pop() if stack else '#'
            if dict[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
