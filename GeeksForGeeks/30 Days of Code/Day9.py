"""
Transfiguration

Professor McGonagall teaches transfiguration at Hogwarts. She has given Harry the task of changing himself into a cat. 
She explains that the trick is to analyze your own DNA and change it into the DNA of a cat. 
The transfigure spell can be used to pick any one character from the DNA string, remove it and insert it in the beginning. 
Help Harry calculates minimum number of times he needs to use the spell to change himself into a cat.

Example 1:

Input: 
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
Output: 3
Explanation:The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS"

Example 2:

Input: 
A = "ABC" 
B = "BCA"
Output: 2
Explanation: The conversion can take place 
in 2 operations:
1. Pick 'C' and place it at the front, 
   A = "CAB"
2. Pick 'B' and place it at the front, 
   A = "BCA"


Your Task:  
You don't need to read input or print anything. Complete the function transfigure() 
which takes strings A and B as input parameters and returns the minimum number of spells needed. 
If it is not possible to convert A to B then return -1.

Expected Time Complexity: O(max(|A|, |B|))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |A|, |B| ≤ 105
A and B consists of lowercase and uppercase letters of english alphabet only.
"""

# Python program to find the minimum number of 
# operations required to transform one string to other 

# Function to find minimum number of operations required 
# to transform A to B 
class Solution():

    def transfigure(self,A, B): 
    	m = len(A) 
    	n = len(B) 

    	# This part checks whether conversion is possible or not 
    	if n != m: 
    		return -1

    	count = [0] * 256

    	for i in range(n):	 # count characters in A 
    		count[ord(B[i])] += 1
    	for i in range(n):	 # subtract count for every char in B 
    		count[ord(A[i])] -= 1
    	for i in range(256): # Check if all counts become 0 
    		if count[i]: 
    			return -1

    	# This part calculates the number of operations required 
    	res = 0
    	i = n-1
    	j = n-1	
    	while i >= 0: 
        
    		# if there is a mismatch, then keep incrementing 
    		# result 'res' until B[j] is not found in A[0..i] 
    		while i>= 0 and A[i] != B[j]: 
    			i -= 1
    			res += 1

    		# if A[i] and B[j] match 
    		if i >= 0: 
    			i -= 1
    			j -= 1

    	return res 

# Driver program 
A = "EACBD"
B = "EABCD"
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
A = "ABC" 
B = "BCA"

obj = Solution()
print(obj.transfigure(A,B))

"""
Hints = 
Firsly, we need to check whether such a conversion is possible or not, the frequency of all the elements in 
A must be same as the frequency of all the elements in B.

Start matching from last characters of both strings. If last characters match, then our task reduces to remaining characters. 
If last characters don’t match, then find the position of B’s mismatching character in A. 
The difference between two positions indicates that these many characters of A must be moved.

"""

# Spoiler
#Back-end complete function Template for Python 3

class Solution:
    def transfigure(self, A, B): 
        m = len(A) 
        n = len(B) 
    
        # Check whether conversion is possible or not 
        if n != m: 
            return -1
    
        count = {}
        keys = count.keys()
    
        # count characters in A 
        for i in A:
            if i in keys:
                count[i] += 1
            else:
                count[i] = 1
    
        # subtract count for every char in B 
        for i in B:
            if i in keys:
                count[i] -= 1
            else:
                count[i] = 1
    
        # Check if all counts become 0 
        for i in keys:  
            if count[i]: 
                return -1
    
        # Calculate the number of operations required 
        res = 0
        i = n-1
        j = n-1 
        while i >= 0: 
        
            # if there is a mismatch, then keep incrementing 
            # result 'res' until B[j] is not found in A[0..i] 
            while i>= 0 and A[i] != B[j]: 
                i -= 1
                res += 1
    
            # if A[i] and B[j] match 
            if i >= 0: 
                i -= 1
                j -= 1
    
        return res 