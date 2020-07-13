class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        if not orders:
            return []
        from collections import defaultdict
        tables = defaultdict(lambda : defaultdict(int))
        food_names = set()
        for order in orders:
            tables[int(order[1])][order[2]] += 1
            food_names.add(order[2])
        food_names = sorted(list(food_names))
        result = []
        temp = ["Table",]
        for food in food_names:
            temp.append(food)
        result.append(temp)
        for i in range(501):
            if i in tables:
                temp = [str(i), ]
                for food in food_names:
                    temp.append(str(tables[i][food]))
                result.append(temp)
        return result
