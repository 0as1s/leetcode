class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        word_counters = [collections.Counter(w) for w in words]
        letters = collections.Counter(letters)
        n = 1<<len(words)
        dp = [-1]*n
        dp[0] = 0
        for mask in range(n):
            if dp[mask] == -1: continue
            # Calculate used letters
            c = collections.Counter()
            for j in range(len(words)):
                if mask & (1<<j) == 0: continue
                c += word_counters[j]
            left = letters - c 
            for j in range(len(words)):
                if mask & (1<<j) != 0: continue
                if word_counters[j] - left: continue # not enough letters
                dp[mask|(1<<j)] = max(dp[mask|(1<<j)], dp[mask] + sum(score[ord(ch)-ord('a')] for ch in words[j]))
        return max(dp)
