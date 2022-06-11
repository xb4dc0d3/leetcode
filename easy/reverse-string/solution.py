class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s) - 1
        i = 0
        j = n
        while (i < j):
          s[i], s[j] = s[j], s[i]
          i += 1
          j -= 1
        return s
