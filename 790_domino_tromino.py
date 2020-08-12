class Solution:
    def numTilings(self, N: int) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def numWays(n, a, b):
            if n < 0:
                return 0
            if n == 0:
                return 1 if a + b == 0 else 0
            ways = 0
            if a + b == 0:
                ways += numWays(n-1, 0, 0)
                ways += numWays(n-2, 0, 0)
                ways += numWays(n-1, 0, 1)
                ways += numWays(n-1, 1, 0)
            elif a == 1:
                ways += numWays(n-2, 0, 0)
                ways += numWays(n-1, 0, 1)
            elif b == 1:
                ways += numWays(n-2, 0, 0)
                ways += numWays(n-1, 1, 0)
            return ways % 1_000_000_007
        return numWays(N, 0, 0)
