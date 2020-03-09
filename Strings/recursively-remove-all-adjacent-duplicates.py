#code
def remove_current_duplicate(string):
    stack = []
    prev = ""
    last_pop = ""
    length = len(string)
    for i in range(0, length):
        if string[i] != prev:
            stack.append(string[i])
            last_pop = ""
        else: #string[i] == prev
            if (string[i] != last_pop):
                last_pop = stack.pop()
        prev = string[i]
    result = ""
    for i in range(0, len(stack)):
        result = result + stack[i]
    return result

def remove_all_adjacent_duplicates(string):
    new_string = remove_current_duplicate(string)
    if new_string == string:
        return new_string
    return remove_all_adjacent_duplicates(new_string)
    
def read_input():
    T = int(input())
    testcases = []
    case_num = 0

    while (case_num+1) <= T:
        string = input()
        testcases.append(string)
        case_num += 1
    return T, testcases


input_res = read_input()
T = input_res[0]
testcases = input_res[1]
for i in range(0, T, 1):
    string = testcases[i]
    print(remove_all_adjacent_duplicates(string))