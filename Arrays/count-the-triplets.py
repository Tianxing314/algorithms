#https://practice.geeksforgeeks.org/problems/count-the-triplets/0
#code
def count_triplets(N, arr):
    count = 0
    arr.sort()

    for i in range(N-1, 1, -1):
        target = arr[i]
        start = 0
        end = i - 1
        while (start <= end-1):
            total = arr[start] + arr[end]
            if total == target:
                count+=1
                start+=1
                end-=1
            elif total < target:
                start+=1
            else:
                end-=1
    if count == 0:
        count = -1
    print(count)
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
    count_triplets(N, arr)

                