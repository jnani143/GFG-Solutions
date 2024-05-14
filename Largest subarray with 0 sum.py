'''Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i

'''
 def maxLen(self, n, arr):
      ml=0
    	s=0
    	dic={}
    	for i in range(n):
    	    s+=a[i]
    	    if sum==0:
    	        ml=i+1
    	    else:
    	        if s in dic.keys():
    	            ml=max(ml,i-dic[s])
    	        else:
    	            dic[sum]=i;
        return ml
