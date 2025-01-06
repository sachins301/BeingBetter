from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        '''
        0 0 0 1 2+0(2) 3+1(4)

        3,3+8 3,3+5 2,2+3 2,2+1  1,1     0,0
        '''
        boxes = [int(i) for i in boxes]
        pre = [0] * len(boxes)
        ball = boxes[0]
        for i in range(1, len(boxes)):
            pre[i] = ball + pre[i - 1]
            ball += boxes[i]
        post = [0] * len(boxes)
        ball = boxes[-1]
        for i in range(len(boxes) - 2, -1, -1):
            post[i] = ball + post[i + 1]
            ball += boxes[i]
            pre[i] += post[i]
        return pre