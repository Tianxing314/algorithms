#https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0 
#code
def reverse_words(words_arr):
    length = len(words_arr)
    words_arr.reverse()
    res = words_arr[0]
    for i in range(1, length):
        res = res + '.' + words_arr[i]
    print(res)
    return res def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        arr = input().split('.')
        testcases.append(arr)
        case_num += 1
    return T, testcases input_res = read_input() T = input_res[0] 
testcases = input_res[1] for i in range(0, T, 1):
    arr = testcases[i]
    reverse_words(arr)
