# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   replaceWords.py
@Contact :   9824373@qq.com
@Desc    :

            在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。

            现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。

            你需要输出替换之后的句子。

            示例 1:

            输入: dict(词典) = ["cat", "bat", "rat"]
            sentence(句子) = "the cattle was rattled by the battery"
            输出: "the cat was rat by the bat"
            注:

            输入只包含小写字母。
            1 <= 字典单词数 <=1000
            1 <=  句中词语数 <= 1000
            1 <= 词根长度 <= 100
            1 <= 句中词语长度 <= 1000

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/replace-words

@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-13     zhan        1.0         None
'''
from collections import defaultdict
from typing import List

class TriNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TriNode)

class Trie:
    def __init__(self):
        self.root = TriNode()

    def insert(self,word):
        '''
        往字典树中插入单词word
        :param word: str 类型
        :return:
        '''
        curNode = self.root
        for char in word:
            curNode = curNode.children[char]

        curNode.is_word = True

    def search(self,word):
        '''
        搜索word是否在trie字典树种
        :param word: str类型
        :return:
        '''
        curNode = self.root
        for char in word:
            curNode = curNode.children[char]
            if curNode is None: return False
        return curNode.is_word

    def startswith(self, prefix):
        '''
        Returns if there is any word in the trie that starts with the given prefix.
        :param prefix:str类型
        :return:
        '''
        curNode = self.root
        for char in prefix:
            curNode = curNode.children[char]
            if curNode is None: return False
        return True

    def get_prefix(self,word):
        '''
        查找word 在trie中出现的最短前缀
        :param word:
        :return:
        '''
        curNode = self.root
        for i, letter in enumerate(word):
            curNode = curNode.children[letter]
            if curNode is not None and curNode.is_word == True:
                return word[:i+1]
        return ''

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dict:
            trie.insert(word)

        ans = ''
        for word in sentence.split():
            rStr = trie.get_prefix(word)
            if rStr: ans += rStr + ' '
            else:ans += word + ' '

        return ans[:-1]

if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"

    ans = Solution().replaceWords(dict, sentence)
    print(ans)


