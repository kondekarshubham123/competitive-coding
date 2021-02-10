"""
Given a string S and an integer K, the task is to reduce the string by applying the following operation:
Choose a group of K consecutive identical characters and remove them. 
The operation can be performed any number of times until it is no longer possible.

Example 1:

Input:
K = 2
S = "geeksforgeeks"
Output:
gksforgks
Explanation:
Modified String after each step: 
"geegsforgeeks" -> "gksforgks"

Example 2:

Input:
K = 2
S = "geegsforgeeeks" 
Output:
sforgeks
Explanation:
Modified String after each step:
"geegsforgeeeks" -> "ggsforgeks" -> "sforgeks"
"""

'''
# Java Code
// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.math.*;

class Gfg
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.next());
        while(t-- > 0)
        {
            int k = Integer.parseInt(sc.next());
            String s = sc.next();
            Solution T = new Solution();
            System.out.println(T.reduced_String(k, s));
            
        }
    }
}
// } Driver Code Ends


//User function Template for Java


class Solution
{
    public static String reduced_String(int k, String s)
    {
        String regex="([a-z])"+"\\1"+"{"+(k-1)+"}";
        for(int i=1;i<s.length()/2;i++){
            if(s.length()==(s=s.replaceAll(regex,"")).length()){
                break;
            }
        }
        return s;
        // Your code goes here
    }
}
'''
#Back-end complete function Template for Python 3

from collections import deque

class Solution:
    def Reduced_String(self, k, s):
        if k == 1:
            ret = ''
            return ret
        
        q = deque()
        
        for c in s:
            # entries in deque will consist of a char
            # and an integer representing how many times it is repeating
            if len(q) and q[-1][0]==c:
                q[-1][1] += 1           # incrementing count
                if q[-1][1]==k:
                    q.pop()             # popping if count is k
            else:
                q.append( [c,1] )       # adding new character
        
        ret=''
        while len(q):                   # generating output string
            ret += q[0][0] * q[0][1]
            q.popleft()
        
        return ret
"""
Hint :
Iterate over the string and use a stack to keep count of appearaces of every character.

Every element of stack will hold information for the character and its number of consecutive appearances.

If count reaches k, pop the stack entry.
"""