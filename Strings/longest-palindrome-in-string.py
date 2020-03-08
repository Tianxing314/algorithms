#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
#code
def is_palindrome(i, j, string):
    if (i <= j):
        if table[i][j] == 1:
            return True
        elif table[i][j] == 0:
            return False
        elif i == j:
            table[i][j] = 1
            return True
        elif i == j - 1:
            if string[i] == string[j]:
                table[i][j] = 1
                return True
            table[i][j] = 0
            return False
        elif string[i] != string[j]:
            table[i][j] = 0
            return False
        elif string[i] == string[j]:
            if is_palindrome(i+1, j-1, string):
                table[i][j] = 1
                return True
            table[i][j] = 0
            return False
    else: #i > j:
        print("i cannot be greater than j")
        return False

def longest_palindrome(string):
    str_len = len(string)
    for palindrome_len in range(str_len, 0, -1):
        if palindrome_len == 1:
            return string[0]
        for i in range(0, str_len - palindrome_len + 1):
            if (is_palindrome(i, i+palindrome_len-1, string)):
                return string[i:i+palindrome_len]

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
    N = len(string)
    table = [[2 for i in range(N)] for j in range(N)]
    print(longest_palindrome(string))
