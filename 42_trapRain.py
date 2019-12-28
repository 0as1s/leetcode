class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # print(len(height))
        if not height:
            return 0

        stack = []
        total_water = []
        total_height = []
        start = -1
        for i in range(len(height)):
            if height[i] != 0:
                total_height.append(height[i])
                total_water.append(0)
                stack.append((i, height[i]))
                start = i
                break
            total_water.append(0)
            total_height.append(0)
        if start == -1:
            return 0
        temp = start
        for i in range(temp+1, len(height)):
            if height[i] != 0:
                total_height.append(total_height[start] + height[i])
                total_water.append((i-temp-1)*min(height[start], height[i]))
                stack.append((i, height[i]))
                temp = i
                break
            total_water.append(0)
            total_height.append(height[start])
        if start == temp:
            return 0
        # print(total_water)
        for i in range(temp+1, len(height)):
            v = height[i]
            if v == 0:
                total_water.append(total_water[-1])
                total_height.append(total_height[-1])
                continue
            total_height.append(total_height[-1] + v)
            index = 0
            poped = 0
            while len(stack) != 1 and stack[-1][-1] < height[i]:
                index, poped = stack.pop()
            if len(stack) == 1:
                if poped >= height[start]:
                    water = (i - index - 1) * poped + total_water[index] - (total_height[i] - total_height[index]) + height[i]
                else:
                    water = (i - start - 1) * min(v, height[start]) - total_height[i] + height[start] + height[i]
                total_water.append(water)
                stack.append((i, v))
                continue
            else:
                index, last = stack[-1]
                water = total_water[index] + (i - index - 1) * v - (total_height[i] - total_height[index]) + height[i]
                total_water.append(water)
                stack.append((i, v))
        return total_water[-1]


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([2, 0, 2]))
print(s.trap([4, 2, 3]))
