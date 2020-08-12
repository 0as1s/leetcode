class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        total = sum(distance)
        start, destination = min(start, destination), max(start, destination)
        sub = sum(distance[start:destination])
        return min(total-sub, sub)