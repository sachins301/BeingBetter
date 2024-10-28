from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = []
        dic = defaultdict(list)

        for path in paths:
            files = path.split()
            for f in files[1:]:
                content = f.split('(')[-1]
                dic[content].append(files[0] + '/' + f.split('(')[0])
        for k,v in dic.items():
            if len(v) > 1:
                res.append(v)
        return res