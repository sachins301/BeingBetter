from collections import Counter


class MinimumWindowSubstring_76:
    def minWindow(self, s: str, t: str) -> str:
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