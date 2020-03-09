#https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
# function should return the peak element not index to it
def findMid(head):
    slow = head
    fast = head.next
    while (fast != None):
        if fast.next == None:
            return slow.next
        slow = slow.next
        fast = fast.next.next
    return slow

#{
#  Driver Code Starts Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node 

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head 

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head).data)

# } Driver Code Ends
