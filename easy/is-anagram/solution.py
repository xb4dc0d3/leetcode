class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def dictCheck(word):
            d = {}
            for char in word:
                d[char] = d.get(char, 0) + 1
            return d
        
        return dictCheck(s) == dictCheck(t) # fixed because the length is same
        
