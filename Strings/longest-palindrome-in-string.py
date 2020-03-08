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
    for i in range(0, length/2):
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
            if (is_palindrome(i, i+palindrome_len-1, string)):
                return string[i:i+palindrome_len]

################ end of bf solution ######################

#Dynamic Programming solution with memory optimization
#time complexity: O(n^2)
#space complexity: O(n^2)
table = []
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
            if is_palindrome(i+1, j-1, string):
                table[i][j] = 1
                return True
            table[i][j] = 0
            return False
    else: #i > j:
        print("i cannot be greater than j")
        return False

def longest_palindrome_dp(string):
    length = len(string)
    longest_str = ""
    longest_len = 0

    #looking for palindromes with odd number of characters
    for i in range(0, length):
        odd_palindrome = string[i]
        l = i - 1
        r = i + 1
        while(l >= 0 and r < length):
            if string[l] == string[r]:
                odd_palindrome = string[l] + odd_palindrome + string[r]
            else: 
                break
            l-=1
            r+=1
        if (len(odd_palindrome) > longest_len):
            longest_len = len(odd_palindrome)
            longest_str = odd_palindrome

    #looking for palindromes with odd number of characters
    for j in range(0, length):
        even_palindrome = ''
        l = j
        r = j + 1
        while(l >= 0 and r < length):
            if string[l] == string[r]:

                even_palindrome = string[l] + even_palindrome + string[r]
            else: 
                break
            l-=1
            r+=1
        if (len(even_palindrome) > longest_len):
            longest_len = len(even_palindrome)
            longest_str = even_palindrome
    return longest_str

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
    N = len(string)
    table = [[2 for i in range(N)] for j in range(N)]
    print(longest_palindrome_dp(string))
