#https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
#code
def max_continuous_sub(N, arr):
    max_old = arr[0]
    max_new = max_old
    for i in range(1, N):
        max_new = max(arr[i], max_new + arr[i])
        if max_new > max_old:
            max_old = max_new
    print(max_old)
    return

def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        N = int(input())
        arr = input().split()
        case = [N, arr]
        testcases.append(case)
        case_num += 1
    return T, testcases

input_res = read_input()

T = input_res[0]
testcases = input_res[1]


for i in range(0, T, 1):
    case = testcases[i]
    N = case[0]
    arr = case[1]
    for i in range(0, N, 1):
        arr[i] = int(arr[i])
    max_continuous_sub(N, arr)