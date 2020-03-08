#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
#code

#Brute Force solution with optimizations
#time complexity: O(n^2)
#space complexity: O(n) 
#n: number of characters in the given string
def is_palindrome(string):
    length = len(string)
    if length == 1:
        return True
    if length == 0:
        return False
    for i in range(0, length//2):
        if string[i] != string[length-1-i]:
            return False
    return True


def longest_palindrome_bf(string):
    str_len = len(string)
    for palindrome_len in range(str_len, 0, -1):
        if palindrome_len == 1:
            return string[0]
        #search for the longest palindrome start at the length equal to the string length
        #gurantee that the first one found will be the first occurance of the longest palindrome
        for i in range(0, str_len - palindrome_len + 1):
            palindrome = string[i: i+palindrome_len]
            if (is_palindrome(palindrome)):
                return palindrome

################ end of bf solution ######################

#Dynamic Programming solution with memory optimization
#time complexity: O(n^2)
#space complexity: O(n^2)
table = [] #need to be initialize to table[N][N] with all elements equal to 2
def is_palindrome_dp(i, j, string):
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
            if is_palindrome_dp(i+1, j-1, string):
                table[i][j] = 1
                return True
            table[i][j] = 0
            return False
    else: #i > j:
        print("i cannot be greater than j")
        return False

def longest_palindrome_dp(string):
    length = len(string)
    longest_palindrome = ""

    for i in range(0, length):
        for j in range(i, length):
            if (is_palindrome_dp(i, j, string)):
                palindrome = string[i:j+1]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
    return longest_palindrome

################ end of dp solution ######################

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
    #run dp solution
#    N = len(string)
#    table = [[2 for i in range(N)] for j in range(N)]
#    print(longest_palindrome_dp(string))
   
    #run bf solution
    print(longest_palindrome_bf(string))
