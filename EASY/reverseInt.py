#link: https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ##arr = []
        temp = x
        ans = 0
        if (temp < 0):
            sign = '-'
            temp = -temp
        else:
            sign = None
        
        while (temp > 0):
            remain = temp % 10
            temp = temp//10
            ans = ans*10 + remain

        if sign == '-':
            ans = ans * -1
        
        if ans > (pow(2,31) - 1):
            return 0
        else:
            return ans

sol = Solution()
ans = sol.reverse(-123)
print(ans)
        
        