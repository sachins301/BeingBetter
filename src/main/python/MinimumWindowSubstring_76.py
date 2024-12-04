from collections import Counter, defaultdict, deque


class MinimumWindowSubstring_76:

    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        window = defaultdict(int)
        queue = deque()
        tCount = Counter(t)
        need, have = len(tCount), 0
        for i in range(len(s)):
            if s[i] not in t:
                continue
            window[s[i]] += 1
            queue.append(i)
            if window[s[i]] == tCount[s[i]]:
                have += 1
            while have == need:
                l = queue[0]
                if i - l + 1 < len(res) or not res:
                    res = s[l : i+1]
                window[s[l]] -= 1
                if window[s[l]] < tCount[s[l]]:
                    have -= 1
                queue.popleft()
        return res

    def minWindow2(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCode = Counter(t)
        i = 0
        j = len(t) - 1
        res = ""
        sCode = Counter(s[i:j+1])
        while(i <= j and j < len(s)):
            matching = True
            for k, v in tCode.items():
                if sCode[k] < v:
                    matching = False
            if matching == True:
                if res == "" or len(res) > j - i + 1:
                    res = s[i:j+1]
                sCode[s[i]] -= 1
                i += 1
            else:
                if(j + 1 < len(s)):
                    j += 1
                    sCode[s[j]] += 1
                else:
                    sCode[s[i]] -= 1
                    i += 1
            # print(s[i:j+1], res, sCode, matching)

        return res