class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = l[i - 1][j - 1] + l[i - 1][j]

            l.append(row)

        return l