# -*- encoding: utf-8 -*-
'''
@project :   LeetCode
@File    :   networkDelayTime.py
@Contact :   9824373@qq.com
@Desc    :
            有 N 个网络节点，标记为 1 到 N。

            给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

            现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

            注意:

            N 的范围在 [1, 100] 之间。
            K 的范围在 [1, N] 之间。
            times 的长度在 [1, 6000] 之间。
            所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。


            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/network-delay-time
@Modify Time                @Author     @Version    @Desciption
------------                -------     --------    -----------
2020-03-11     zhan        1.0         None
'''
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for s,t,d in times:
            graph[s].append((t,d))

        dist ={}
        #  按距离排序，所以距离放在前面
        pq = [(0,K)]

        # Dijkstra算法 最短路径算法
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d

            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1


if __name__ == '__main__':
    A = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2

    ans = Solution().networkDelayTime(A,N,K)
    print(ans)



