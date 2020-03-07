# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   ladderLength.py
@Contact :   9824373@qq.com
@Desc    :
            给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

            每次转换只能改变一个字母。
            转换过程中的中间单词必须是字典中的单词。
            说明:

            如果不存在这样的转换序列，返回 0。
            所有单词具有相同的长度。
            所有单词只由小写字母组成。
            字典中不存在重复的单词。
            你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
            示例 1:

            输入:
            beginWord = "hit",
            endWord = "cog",
            wordList = ["hot","dot","dog","lot","log","cog"]

            输出: 5

            解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
                 返回它的长度 5。
            示例 2:

            输入:
            beginWord = "hit"
            endWord = "cog"
            wordList = ["hot","dot","dog","lot","log"]

            输出: 0

            解释: endWord "cog" 不在字典中，所以无法进行转换。

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/word-ladder

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-06     zhan        1.0         None
'''
from typing import List
from collections import deque,defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList: return 0
        if beginWord not in wordList: wordList.append(beginWord)
        graph = self.generalDictGraph(wordList)
        flag = {word:0 for word in wordList}
        queue = deque()
        d = 1
        queue.append((beginWord,1))

        while queue:
            curEle = queue.popleft()
            if endWord in {ele for ele in self.neighbors(curEle[0],graph)}:
                return curEle[1] + 1
            else:
                for nextEle in self.neighbors(curEle[0],graph):
                    if flag[nextEle] == 0:
                        queue.append((nextEle,curEle[1]+1))
                        flag[nextEle] = 1

        return 0


    def constructGraph(self,wordList: List[str]):
        graph = {word:set() for word in wordList}
        # graph = set()
        for i, word in enumerate(wordList):
            for j in range(i+1,len(wordList)):
                iCount = 0
                for idx in range(0,len(wordList[i])):
                    if wordList[i][idx] != wordList[j][idx]:
                        iCount += 1
                    if iCount >=2: break

                if iCount == 1:
                    graph[wordList[i]].add(wordList[j])
                    graph[wordList[j]].add(wordList[i])
        return graph

    def generalDictGraph(self,wordList: List[str]):
        graph = defaultdict(set)

        for word in wordList:
            for j in range(len(word)):
                graph[word[:j] + "*" + word[j+1:]].add(word)
        return graph

    def neighbors(self,word,graph):
        for j in range(len(word)):
            for neighbor in graph[word[:j] + "*" + word[j+1:]]:
                if neighbor != word:
                    yield neighbor


if __name__ == '__main__':
    beginWord   = "hit"
    endWord     = "cog"
    wordList    = ["hot","dot","dog","lot","log"]
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans = Solution().ladderLength(beginWord,endWord,wordList)
    print(ans)


