# Count Triplets 
'''
Given a sorted linked list of distinct nodes (no two nodes have the same data) and an integer X. 
Count distinct triplets in the list that sum up to given integer X.


Example 1:

Input: LinkedList: 1->2->4->5->6->8->9, X = 17
Output: 2
Explanation: Distinct triplets are (2, 6, 9) 
and (4, 5, 8) which have sum equal to X i.e 17.

Example 2:

Input: LinkedList: 1->2->4->5->6->8->9, X = 15
Output: 5
Explanation: (1, 5, 9), (1, 6, 8), (2, 4, 9), 
(2, 5, 8), (4, 5, 6) are the distinct triplets

Your Task:  
You don't need to read input or print anything. 
Complete the function countTriplets() which takes a head reference and X as input 
parameters and returns the triplet count

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ Number of Nodes ≤ 103 
1 ≤ Node value ≤ 104
'''
#User function Template for python3

def countTriplets(head,x):
    ptr2=head
    count = 0;
  
    # unordered_map 'um' implemented as hash table
    um = dict()
     
    ptr = head
    # insert the <node data, node pointer> tuple in 'um'
    while ptr!=None:
        um[ptr.val] = ptr;
        ptr = ptr.nxt
  
    # generate all possible pairs
    ptr1=head
     
    while ptr1!=None:
         
        ptr2 = ptr1.nxt
         
        while ptr2!=None:
  
            # p_sum - sum of elements in the current pair
            p_sum = ptr1.val + ptr2.val;
  
            # if 'x-p_sum' is present in 'um' and either of the two nodes
            # are not equal to the 'um[x-p_sum]' node
            if ((x-p_sum) in um) and um[x - p_sum] != ptr1 and um[x - p_sum] != ptr2:
  
                # increment count
                count+=1
            ptr2 = ptr2.nxt
        ptr1 = ptr1.nxt
         
  
    # required count of triplets
    # division by 3 as each triplet is counted 3 times
    return (count // 3);



#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        x = int(line[1])
        line = input().strip().split()
        
        head = Node(int(line[0]))
        tail = head
        for i in range(1,n):
            tail.nxt = Node(int(line[i]))
            tail = tail.nxt
        
        print(countTriplets(head,x))


# } Driver Code Ends
"""
HINT:
Think how hashing will work here!

#Back-end complete function Template for Python 3

from collections import deque 

def countPairs(head,x):
    if head==None or head.nxt==None or x<2:
        return 0
    dq = deque()
    walk = head
    while walk:
        dq.append(walk.val)
        walk=walk.nxt
    
    ret=0
    l=dq.popleft()
    r=dq.pop()
    while(1):
        if l+r==x:
            ret+=1
        if len(dq)==0:
            return ret
        if l+r>x:
            l=dq.popleft()
        else:
            r=dq.pop()

def countTriplets(head,x):
    ret = 0
    while head != None:
        ret += countPairs(head.nxt, x-head.val)
        head = head.nxt
    return ret

"""