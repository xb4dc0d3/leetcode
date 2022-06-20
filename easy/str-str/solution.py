class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_needle = len(needle)

        f_index = 0

        if needle == "":
            return 0

        while (f_index <= len(haystack) - 1):

            if haystack[f_index:f_index+len_needle] == needle:
                return f_index

            else:
                f_index += 1
        return -1
