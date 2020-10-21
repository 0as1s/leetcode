from typing import List
import functools

def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # 1. Optimization: If a string is length 1, always use it.
        count = 0
        strings = []
        for i in range(len(strs)):
            if (len(strs[i]) == 1):
                if (strs[i] == '0') and m:
                    m -= 1
                    count += 1
                    continue
                elif (strs[i] == '1') and n:
                    n -= 1
                    count += 1
                    continue
            strings.append(strs[i])
            
        # 2. Optimization: Keep a hashtable of string_id -> number of ones in the string
        ones = {}
        zeros = {}
        for i in range(len(strings)):
            ones[i] = strings[i].count('1')
            zeros[i] = len(strings[i]) - ones[i]
        
        # 3. Memoization
        # 3.1 If we have used more 0 or 1 than allowed, return -1 to account for the string we should not have added.
        # 3.2 If i == len(strings), then we have considered every string, return 0 because there are no more strings for us to try adding.
        # 3.3 Try including and not including the string, return the option that yields the best result.
        @functools.lru_cache(None)
        def helper(i, m, n):
            if (m < 0) or (n < 0): return -1                                      # 3.1
            if i == len(strings): return 0                                        # 3.2
            return max(helper(i+1, m, n), 1 + helper(i+1, m-zeros[i], n-ones[i])) # 3.3
        
        return count + helper(0, m, n)