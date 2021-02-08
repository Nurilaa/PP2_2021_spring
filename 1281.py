class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    sum = 0
    sum2 = 1
    for i in str(n):
      sum += int(i)
      sum2 *= int(i)
    return sum2 - sum