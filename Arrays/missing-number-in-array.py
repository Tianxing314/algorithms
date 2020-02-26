#https://practice.geeksforgeeks.org/problems/missing-number-in-array/0 
#code
def missing_number_in_array(N, arr):
    total = 0
    for i in range(1, N+1):
        total+=i
    for i in range(0, N-1):
        total-=arr[i]
    print(total)
    return total
    
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
    return T, testcases input_res = read_input() T = input_res[0] 
testcases = input_res[1] for i in range(0, T, 1):
    case = testcases[i]
    N = case[0]
    arr = case[1]
    for i in range(0, N-1, 1):
        arr[i] = int(arr[i])
    missing_number_in_array(N, arr)
