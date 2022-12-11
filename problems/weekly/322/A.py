class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        N = len(words)
        for i in range(N):
            if i == N-1:
                if words[i][-1] != words[0][0]:
                    return False
            else:
                if words[i][-1] != words[i+1][0]:
                    return False

        return True
        
