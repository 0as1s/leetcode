
class Solution:
    def originalDigits(self, s: str) -> str:
        digits = {
         'z': [0],
         'w': [2],
         'u': [4],
         'x': [6],
         'g': [8],
         'h': [8, 3],
         'f': [4, 5],
         's': [6, 7],
         'o': [0, 2, 4, 1],
         'i': [5, 6, 8, 9],
        }
        counts = [0] * 10
        for c in s:
            if c in digits:
                counts[digits[c][-1]] += 1
        for c in 'hfsoi':
            counts[digits[c][-1]] -= sum(counts[i] for i in digits[c][:-1])
        return ''.join([str(i) * c for i, c in enumerate(counts) if c])