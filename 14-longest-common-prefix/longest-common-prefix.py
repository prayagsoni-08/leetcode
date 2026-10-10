class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        l = strs[0]

        for i in strs[1:]:
            j = 0
            while j < len(l) and j < len(i) and l[j] == i[j]:
                j += 1

            l = l[:j]
            if not l:
                return ""

        return l