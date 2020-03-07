#https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
#code
def longest_palindrome(string):
    longest_str = ''
    longest_len = 0
    
    length = len(string)
    is_odd = (True if length%2 == 1 else False)
    
    if length == 0:
        print('')
        return 
    
    #odd_palindrome
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
    
    #even_palindrome
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
    
    if longest_len == 0: #return the first char if there is no palindrome string with length larger than 1
        longest_str = string[0]
    print(longest_str)
    return
        
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
    longest_palindrome(string)