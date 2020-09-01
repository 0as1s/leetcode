class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # 1 2 3 = 6
        # 5 7 9 = 18
        # 12 15 18 = 18+27
        # 1 + (1+num_people) + (1+num_people+num_people) = (n + (n-1)*num_people) = x
        # [x, x+n, x+2n, x+3n...] = sum
        # (n + (n-1)*num_people) * n + (n + (n-1)*n) * (n-1) //2 = sum
        n = 1
        if sum(range(1, num_people+1)) > candies:
            r = [0] * num_people
            candy = 1
            left = candies
            i = 0
            while left > 0:
                if left > candy + i:
                    r[i] += candy + i
                    left -= (candy + i)
                else:
                    r[i] += left
                    break
                i += 1
            return r
            
        while True:
            print((n + (n-1)*num_people) * num_people + (n + (num_people-1)*n) * (num_people-1) //2)
            if (n + (n-1)*num_people) * num_people + (n + (num_people-1)*n) * (num_people-1) //2 >= candies:
                l = n-1
                first = l + (l-1) * num_people
                print(first)
                r = [first + i*l for i in range(num_people)]
                print(r)
                candy = 1 + (l*num_people)
                left = candies - sum(r)
                i = 0
                while left > 0:
                    if left > candy + i:
                        r[i] += candy + i
                        left -= (candy + i)
                    else:
                        r[i] += left
                        break
                    i += 1
                return r
            n += 1
s = Solution()
print(s.distributeCandies(96, 5))
print(s.distributeCandies(94, 5))
