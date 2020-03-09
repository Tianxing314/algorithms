#https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places/0 
#code
def check_rotation(string, target_str):
    length = len(string)
    if length <= 2:
        return 1 #True
    cw_str = string[length-2:length] + string[:length-2]
    ccw_str = string[2:length] + string[:2]
    if cw_str == target_str:
        return 1
    if ccw_str == target_str:
        return 1
    return 0 #Default to False 

def read_input():
    T = int(input())
    testcases = []
    case_num = 0
    while (case_num+1) <= T:
        string = input()
        target = input()
        testcase = [string, target]
        testcases.append(testcase)
        case_num += 1
    return T, testcases 

if __name__=='__main__':
    input_res = read_input() 
    T = input_res[0] 
    testcases = input_res[1] 

    for i in range(0, T, 1):
        string = testcases[i][0]
        target_str = testcases[i][1]
        print(check_rotation(string, target_str))
