from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        以排序后的字符串为key键hash表。
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sort_strs = defaultdict(list)


        for s in strs:
            tmps = tuple(sorted(s))
            sort_strs[tmps].append(s)

        rst = []
        for k, v in sort_strs.items():
            rst.append(v)

        return rst

if __name__ == '__main__':

    a = ["eat","tea","tan","ate","nat","bat"]
    rst = Solution().groupAnagrams(a)
    print(rst)