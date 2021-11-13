def generateParenthesis(n):
  if (n == 0): return []
  return helper('', n, 0)

def helper(curr, numAvailable, numUnclosed):
  if numAvailable == 0:
  	return [curr + ')' * numUnclosed]
  elif numUnclosed == 0:
    return helper(curr + '(', numAvailable - 1, numUnclosed + 1)
  return helper(curr + '(', numAvailable - 1, numUnclosed + 1) + helper(curr + ')', numAvailable, numUnclosed - 1)

d = generateParenthesis(3)
print(d)