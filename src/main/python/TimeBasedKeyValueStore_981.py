class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp, value))
        else:
            self.dic[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        res_list = self.dic[key]
        l, r = 0, len(res_list) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp > res_list[mid][0]:
                l = mid + 1
            elif timestamp < res_list[mid][0]:
                r = mid - 1
            else:
                return res_list[mid][1]
        print(timestamp, l, r, res_list[r][1])
        return "" if r < 0  else res_list[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)