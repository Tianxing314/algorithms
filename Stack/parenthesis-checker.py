#https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
#code
def check_balance(string):
    length = len(string)
    if length%2 != 0:
        return False
    left = ["{", "[", "("]
    right = ["}", "]", ")"]
    stack = ["bottom"]
    
    for i in range(0, length):
        character = string[i]
        if character in left:
            stack.append(character)
        else: #character in right
            p_index = right.index(character)
            top = stack.pop()
            if top == "bottom":
                return False
            if left.index(top) != p_index:
                return False
        
    if len(stack) != 1:
        return False
    return True

def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        string = input()
        testcases.append(string)
        case_num += 1
    return T, testcases

if __name__=='__main__':
    input_res = read_input()
    T = input_res[0]
    testcases = input_res[1]

    for i in range(0, T, 1):
        string = testcases[i]
        if(check_balance(string)):
            print("balanced")
        else:
            print("not balanced")     