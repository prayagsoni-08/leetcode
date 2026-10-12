class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

        if not s:
            return 0

        c = 0
        a = len(s) - 1

        for i in range(len(s) - 1, -1, -1):
            if int(d[s[i]]) < int(d[s[a]]):
                c -= int(d[s[i]])
            else:
                c += int(d[s[i]])

            a = i

        return c