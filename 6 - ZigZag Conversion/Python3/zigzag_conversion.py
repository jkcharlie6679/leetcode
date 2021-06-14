class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) <= numRows or numRows == 1:
            return s
        
        zig = [''] * numRows
        index, step = 0, 1

        for x in s:
            zig[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(zig)