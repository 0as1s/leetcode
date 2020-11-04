class Solution:
    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        res = [0]*len(people)
        people.sort(key=lambda x: [x[0], -x[1]])
        pos = [i for i in range(len(people))]
        while people:
            v, i = people.pop(0)
            res[pos[i]] = [v, i]
            pos.remove(pos[i])
        return res
