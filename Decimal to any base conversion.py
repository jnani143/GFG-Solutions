Given a decimal number N and the base B to which it should be converted. Convert the given number to the given base.
Example 1:

Input:
B = 2
N = 12 

Output:
1100

Explanation:
If the number 12 is converted to a 
number with base 2 we get the binary 
representation of 12 = 1100.

class Solution:
    def getNumber(self, B, N):
    	#code here 
        dic={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    	rem=0
    	result=""
    	temp=""
    	while(N>0):
    	
    	    rem=N%B
    	    if rem>9:
    	        temp=dic[rem]
    	    else:
    	        temp=str(rem)
    	    result+=temp
    	    N=N//B
    	return result[::-1]
