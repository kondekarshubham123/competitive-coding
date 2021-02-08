# https://www.geeksforgeeks.org/check-if-given-preorder-inorder-and-postorder-traversals-are-of-same-tree-set-2/
# https://ide.geeksforgeeks.org/s8qoZ94cUJ
# Python program to check if the given
# three traversals are of the same
# tree or not

# Function to check if all three traversals
# are of the same tree

class Solution(object):
    def checktree(self,preorder, inorder, postorder, length):

    	# if the array lengths are 0,
    	# then all of them are obviously equal
    	if length == 0:
    		return 1

    	# if array lengths are 1,
    	# then check if all of them are equal
    	if length == 1:
    		return (preorder[0] == inorder[0]) and
    			(inorder[0] == postorder[0])

    	# search for first element of preorder
    	# in inorder array
    	idx = -1

    	for i in range(length):
    		if inorder[i] == preorder[0]:
    			idx = i
    			break

    	if idx == -1:
    		return 0

    	# check for the left subtree
    	ret1 = self.checktree(preorder[1:], inorder, postorder, idx)

    	# check for the right subtree
    	ret2 = self.checktree(preorder[idx + 1:], inorder[idx + 1:],
    					postorder[idx:], length-idx-1)

    	# return 1 only if both of them are correct else 0
    	return (ret1 and ret2)


# Driver Code
if __name__ == "__main__":
	inorder = [4, 2, 5, 1, 3]
	preorder = [1, 2, 4, 5, 3]
	postorder = [4, 5, 2, 3, 1]
	len1 = len(inorder)
	len2 = len(preorder)
	len3 = len(postorder)

	# check if all the array lengths are equal
	if (len1 == len2) and (len2 == len3):
		correct = checktree(preorder, inorder,
							postorder, len1)
		if (correct):
			print("Yes")
		else:
			print("No")
	else:
		print("No")

"""
HINTS:
The root element will be the first element of preorder.
Search for root in the inorder array and store it’s index as idx. 
Use this idx to determine elements of left and right subtree in all three traversal arrays. 
Call function recursively for both left and right sub tree.

#Back-end complete function Template for Python 3


class Solution:
    def checktree(self, preorder, inorder, postorder, N): 
	
    	# if the array lengths are 0, then all of them are obviously equal 
    	if N == 0: 
    		return 1
    		
    	# if array lengths are 1, then check if all of them are equal 
    	if N == 1: 
    		return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0]); 
    
    	# search for first element of preorder in inorder array 
    	idx = -1; 
    	
    	for i in range(N): 
    		if inorder[i] == preorder[0]: 
    			idx = i 
    			break
    	
    	if idx == -1: 
    		return 0;
    	
    	# matching element in postorder array
    	if preorder[0] != postorder[N-1]:
    	    return 0;
    	
    	# check for the left subtree 
    	ret1 = self.checktree(preorder[1:], inorder, postorder, idx); 
    	
    	# check for the right subtree	 
    	ret2 = self.checktree(preorder[idx + 1:], inorder[idx + 1:], 
    						postorder[idx:], N-idx-1); 
    	
    	# return 1 only if both of them are correct else 0 
    	return (ret1 and ret2) 
"""