from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastChar = defaultdict(int)
        for i in range(len(s)):
            if lastChar[s[i]] < i:
                lastChar[s[i]] = i
        end = 0
        size = 0
        res = []
        for i, c in enumerate(s):
            if lastChar[c] > end:
                end = lastChar[c]
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res

    def partitionLabels(self, s: str) -> List[int]:
        '''
        ababc
        {[0, 2], [1, 3], [4, 4]}
        [0, 2], [0, 2], [0, 2], [0, 3], [4, 4]
        create a dic of start and end position
        create a list
        set part start as the first occurence
        if start less than prev end, replace start with prev start
        set end pos of curr alpha
        '''
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = [i, i]
            dic[s[i]][1] = i
        partition = []
        for i in range(len(s)):
            part = [dic[s[i]][0], dic[s[i]][1]]
            if i > 0 and partition[-1][1] > part[0]:
                part[0] = partition[-1][0]
                part[1] = max(part[1], partition[-1][1])
                partition.pop()
            partition.append(part)
        # print(partition)
        return [p[1] - p[0] + 1 for p in partition]