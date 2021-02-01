from functools import lru_cache

@lru_cache
def helper(digits, n_str):
    head = int(n_str[0])
    less_than = len([x for x in digits if x < head])
    less_than *= len(digits) ** (len(n_str) - 1)

    if head in digits:
        return helper(digits, n_str[1:]) + less_than
    print(less_than)
    return less_than

class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        n_str = str(n)
        zeros = [len(digits) ** i  for i in range(1, len(n_str))]
        return sum(zeros) + helper(tuple([int(x) for x in digits]), n_str)
