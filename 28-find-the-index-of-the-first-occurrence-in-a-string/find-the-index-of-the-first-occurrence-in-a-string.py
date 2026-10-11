class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) ==1 and len(needle)==1:
            if haystack[0]==needle[0]:
                return 0
            return -1
        if len(haystack) < len(needle):
            return -1
        else:
            if needle in haystack:
                for i in range(len(haystack)):
                    if needle[0::]==haystack[i:len(needle)+i]:
                        return i
            else:
                return -1
        