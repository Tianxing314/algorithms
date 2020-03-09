#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0  

#code
def sub_arr(N, S, arr):
    start = 0
    end = 0
    temp_S = arr[0]
    while end <= N-1:
        if temp_S == S:
            print(str(start+1) + " " + str(end+1))
            return
        elif temp_S < S:
            if end == N-1:
                print(str(-1))
                return
            end += 1
            temp_S += arr[end]
        else:
            temp_S -= arr[start]
            start += 1
    print("-1")
    return

def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        N_S = input().split()
        N = int(N_S[0])
        S = int(N_S[1])
        arr = input().split()
        case = [N, S, arr]
        testcases.append(case)
        case_num += 1
    return T, testcases

if __name__=='__main__':
    input_res = read_input()
    T = input_res[0]
    testcases = input_res[1]

    for i in range(0, T, 1):
        case = testcases[i]
        N = case[0]
        S = case[1]
        arr = case[2]
        for i in range(0, N, 1):
            arr[i] = int(arr[i])
        sub_arr(N, S, arr)
