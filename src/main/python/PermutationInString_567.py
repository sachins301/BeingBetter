class PermutationInString_567:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Code = [0]*26
        for c in s1:
            s1Code[ord(c) - ord('a')] += 1
        i = 0
        j = len(s1) - 1
        s2Code = [0]*26
        for c in s2[i:j+1]:
            s2Code[ord(c) - ord('a')] += 1
        if s1Code == s2Code:
            return True
        j += 1
        while j < len(s2):
            s2Code[ord(s2[i]) - ord('a')] -= 1
            i += 1
            s2Code[ord(s2[j]) - ord('a')] += 1
            if s1Code == s2Code:
                return True
            j += 1

        return False