#https://practice.geeksforgeeks.org/problems/palindrome-string/0
#code
def is_palindrome(string):
    length = len(string)
    if length <= 1:
        return True
    for i in range(0, length//2-1):
        if (string[i] != string[length-i-1]):
            return False 
    return True

def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        N = input()
        string = input()
        testcases.append(string)
        case_num += 1
    return T, testcases

if __name__=='__main__':
    input_res = read_input()
    T = input_res[0]
    testcases = input_res[1]

    for i in range(0, T, 1):
        string = testcases[i]
        if(is_palindrome(string)):
            print("Yes")
        else:
            print("No")