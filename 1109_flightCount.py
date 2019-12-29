from typing import List
from collections import defaultdict

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        bookings = sorted(bookings)
        d = defaultdict(int)
        result = []
        cur = 0
        i_flight = 0
        for i_book in range(1, n+1):
            cur -= d[i_book-1]
            while i_flight < len(bookings):
                i, j, k = bookings[i_flight]
                if i > i_book:
                    break
                cur += k
                d[j] += k
                i_flight += 1
            result.append(cur)

        return result

bookings = [[2,2,35],[1,2,10]]
n=2
s = Solution()
print(s.corpFlightBookings(bookings, n))
