from queue import Queue


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return []
        squence = Queue()
        for i in range(len(deck)):
            squence.put(i)
        temp = []
        while True:
            v = squence.get()
            if squence.empty():
                temp.append(v)
                break
            temp.append(v)
            v = squence.get()
            if squence.empty():
                temp.append(v)
                break
            squence.put(v)
        result = [0] * len(deck)
        deck = sorted(deck)
        for i in range(len(result)):
            result[temp[i]] = deck[i]
        return result

s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))