# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   minimumLengthEncoding.py
@Contact :   9824373@qq.com
@Desc    :
                给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

                例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

                对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

                那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

                 

                示例：

                输入: words = ["time", "me", "bell"]
                输出: 10
                说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
                 

                提示：

                1 <= words.length <= 2000
                1 <= words[i].length <= 7
                每个单词都是小写字母 。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/short-encoding-of-words

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-28     zhan        1.0         None
'''
from typing import List
import collections
from functools import reduce

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # return self.minimumLengthEncoding_sort(words)
        return self.minimumLengthEncoding_trie(words)

    def minimumLengthEncoding_sort(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=lambda word:word[::-1])

        S = ''
        i = 0
        while i < len(words):
            while i < len(words)-1 and len(words[i]) <= len(words[i+1]) and words[i] == words[i+1][-len(words[i]):]:
                i +=1
            S += words[i]
            S += '#'
            i += 1

        return len(S)

    def minimumLengthEncoding_trie(self, words: List[str]) -> int:
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        # nodes = []
        # for word in words:
        #     v = reduce(dict.__getitem__, word[::-1], trie)
        #     nodes.append(v)
        # 构建 trie ，同时对于前缀，返回非控制，对于取到叶节点，返回空值
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]


        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)


if __name__ == '__main__':
    words = ["me", "time", "bell"]

    ans = Solution().minimumLengthEncoding(words)
    print(ans)


