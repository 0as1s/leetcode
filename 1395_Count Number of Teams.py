""" class Solution(object):
    def numTeams(self, rating):
        
        :type rating: List[int]
        :rtype: int
        if not rating or len(rating)<3:
            return 0
        
        lt_arr = [0, ] * len(rating)
        gt_arr = [0, ] * len(rating)
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                if rating[j] > rating[i]:
                    gt_arr[i] += 1
                else:
                    lt_arr[i] += 1
        sum = 0
        for i in range(len(rating)):
            for j in range(1, len(rating)):
                if rating[j] > rating[i]:
                    sum += gt_arr[j]
                else:
                    sum += lt_arr[j]
        return sum
 """
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        if not rating or len(rating)<3:
            return 0
        
        lt_arr = [0, ] * len(rating)
        gt_arr = [0, ] * len(rating)
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                if rating[j] > rating[i]:
                    gt_arr[i] += 1
                if rating[j] < rating[i]:
                    lt_arr[i] += 1
        print(gt_arr)
        print(lt_arr)
        sum = 0
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                if rating[j] > rating[i]:
                    sum += gt_arr[j]
                if rating[j] < rating[i]:
                    sum += lt_arr[j]
        return sum

