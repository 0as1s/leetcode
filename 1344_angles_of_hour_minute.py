class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        m_a = (float(minutes) / 60.0) * 360.0
        if hour>12:
            hour -= 12
        h_a = (float(hour) / 12.0) * 360.0 + (1.0/12.0) * (float(minutes)/60.0) * 360.0
        return abs(min(max(m_a, h_a) - min(m_a, h_a), 360.0 - (max(m_a, h_a) - min(m_a, h_a))))