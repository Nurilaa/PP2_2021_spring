class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        h = 0
        for i in gain:
          h += i;
          if h > res:
            res = h
        return res
