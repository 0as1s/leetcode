class Solution(object):
    def helper(self, s, result, cur_list, cur_ip):
        if cur_ip and int(cur_ip) > 255:
            return
        if cur_ip and len(cur_ip) != 1 and cur_ip[0] == "0":
            return
        if not s:
            if len(cur_list) == 3 and cur_ip:
                cur_list.append(cur_ip)
                print(cur_list)
                result.append(cur_list)
                return
            else:
                return
        if len(cur_list) == 4:
            return
        
        self.helper(s[1:], result, list(cur_list), cur_ip+s[0])
        if cur_ip:
            cur_list.append(cur_ip)
            self.helper(s, result, list(cur_list), "")
        
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.helper(s, result, [], "")
        return [".".join(x) for x in result]


s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("101023"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("0000"))

