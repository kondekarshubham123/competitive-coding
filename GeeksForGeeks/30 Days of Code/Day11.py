# Secret Cipher{Hard}
'''
Geek wants to send an encrypted message in the form of string S to his friend Keeg 
along with instructions on how to decipher the message. To decipher the message, his friend 
needs to iterate over the message string from left to right, if he finds a '*', he must 
remove it and add all the letters read so far to the string. He must keep on doing this till 
he gets rid of all the '*'.
Can you help Geek encrypt his message string S? 

Note: If the string can be encrypted in multiple ways, find the smallest encrypted string. 

Example 1:

Input: S = "ababcababcd"
Output: ab*c*d
Explanation: We can encrypt the string 
in following way : "ababcababcd" -> 
"ababc*d" -> "ab*c*d"

Example 2:

Input: S = "zzzzzzz"
Output: z*z*z
Explanation: The string can be encrypted 
in 2 ways: "z*z*z" and "z**zzz". Out of 
the two "z*z*z" is smaller in length.

Your Task: 
You don't need to read input or print anything. Complete the function 
secretCipher() which takes the message string S as input parameter and returns the 
shortest possible encrypted string.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints: 
1 ≤ |S| ≤ 105

'''

# class Solution{
    # public:
    # string compress(string s)
    # {
        # int n=s.size();
        # vector<int>v(n);
        # for(int i = 1;i<n;i++){
            # int j=v[i-1];
            # while(j>0 && s[i]!=s[j]){
                # j = v[j-1];
            # }
            # if(s[i]==s[j]) j++;
            # v[i]=j;
        # }
        # string ans;
        # for(int i=n-1;i>=0;i--){
            # if(i%2){
                # if(v[i]>=(i+1)/2 && (i+1)%(2*(i+1-v[i]))==0){
                    # ans.push_back('*');
                    # i/=2;i++;
                # }
                # else{
                    # ans.push_back(s[i]);
                # }
            # }
            # else{
                # ans.push_back(s[i]);
            # }
        # }
        # reverse(ans.begin(),ans.end());
        # return ans;
        # // Your code goes here
    # }
# };

"""
Hint :
Find the longest proper prefix which is also a proper suffix for each prefix of the string.
"""
#Back-end complete function Template for Python 3

class Solution:
    def fillarray(self, s, a):
        a[0]=0
        for i in range(1,len(s)):
            series=a[i-1]
            while(series):
                if(s[series]==s[i]):
                    a[i]=series+1
                    break
                series=a[series-1]
            if(series==0):
                a[i]=(int(s[i]==s[0]))
        return a
        
    def compress(self, s):
        a=[0]*len(s)
        
        #  ith element of array a stores the length of longest
        #  proper suffix which is also a proper prefix
        #  for substr s[0] to s[i]
        a = self.fillarray(s, a)
        #print(a)
        shortened=[]
        n=len(s)
        i=n-1
        
        #  for even index, string length is odd
        #  hence it cannot be divided into two
        #  so we simply push ith character in stack
        while(i>0):
            if(i%2==0):
                shortened.append(s[i])
                i=i-1
                continue
            
            # star_here will be made TRUE if substring s[0] to s[i]
            # can be divided into identical halves
            star_here=False
            
            #  suffix and substring length are also meant for
            #  substring s[0] to s[i]
            suffix=a[i]
            substrlen=i+1
            
            #  these conditions, if true, imply that, substring
            #  can be divided into 2 identical halves
            if(suffix*2>=substrlen):
                if(substrlen%(substrlen-suffix)==0):
                    if((substrlen/(substrlen-suffix))%2==0):
                        star_here=True
                        
            
            #  adding * to stack and moving index as required
            if(star_here==True):
                shortened.append('*')
                i=(i//2)+1
                
            #  else, simply adding character to stack
            else:
                shortened.append(s[i])
            i=i-1
        ret=""
        ret=ret+s[0]
        n=len(shortened)
        
        #  since we analysed input string from end to start
        #  removing elements from stack and pushing back to
        #  output string will reverse them back to required order
        while(n):
            ret=ret+shortened[n-1]
            shortened.pop()
            n=n-1
        return ret
    