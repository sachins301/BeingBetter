class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        res = [[-1] * COLS for _ in range(ROWS)]
        visit = set()
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    visit.add((i, j))
                    res[i][j] = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            r, c = q.popleft()
            h = res[r][c]
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    res[nr][nc] = h + 1
        return res