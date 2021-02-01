class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        position = {}
        for i, line in enumerate(["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]):
            for j, l in enumerate(line):
                position[l] = (i, j)
        target = "a" + target
        result = ""
        for i in range(1, len(target)):
            f, t = target[i-1], target[i]
            if t == "z":
                delta_y = position[t][1] - position[f][1]
                if delta_y > 1:
                    result += abs(delta_y) * "R"
                else:
                    result += abs(delta_y) * "L"
                delta_x = position[t][0] - position[f][0]
                if delta_x > 0:
                    result += abs(delta_x) * "U"
                else:
                    result += abs(delta_x) * "D"
            else:
                delta_x = position[t][0] - position[f][0]
                if delta_x > 0:
                    result += abs(delta_x) * "U"
                else:
                    result += abs(delta_x) * "D"
                delta_y = position[t][1] - position[f][1]
                if delta_y > 1:
                    result += abs(delta_y) * "R"
                else:
                    result += abs(delta_y) * "L"
            result += "!"
        return result
