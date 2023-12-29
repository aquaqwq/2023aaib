class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        H = {}
        for C in chars:
            if C in H: H[C] += 1
            else:      H[C] = 1

        for word in words:
            wordH = {}
            for C in word:
                if C in wordH: wordH[C] += 1
                else:          wordH[C] = 1
            
            bad = 0
            for C in wordH:
                if(C not in H) or wordH[C]>H[C]:
                    bad = 1
            if bad ==0: ans += len(word)

        return ans