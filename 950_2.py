from queue import deque


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck = reversed(sorted(deck))
        q = deque()
        for d in deck:
            if not q:
                q.append(d)
            else:
                q.appendleft(q.pop())
                q.appendleft(d)
        return q