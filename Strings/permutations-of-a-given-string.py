#https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0 code
def permutation(i, string, dictionary):
    length = len(string)
    fixed = string[0:i]
    if i == length - 1:
        return
    for j in range(i, length):
        temp_str = fixed + string[j] + string[i:j] + string[j+1::]
        #check with dictionary to avoid duplicates
        if dictionary.get(temp_str) != 1:
            dictionary[temp_str] = 1
            print(temp_str)
        permutation(i+1, temp_str,dictionary)
        
def read_input():
    T = int(input())
    testcases = []
    case_num = 0
   
    while (case_num+1) <= T:
        string = input()
        testcases.append(string)
        case_num += 1
    return T, testcases 

if __name__=='__main__':
    input_res = read_input() 
    T = input_res[0] 
    testcases = input_res[1]
    for i in range(0, T, 1):
        dictionary = {}
        string = testcases[i]
        permutation(0, string, dictionary)
