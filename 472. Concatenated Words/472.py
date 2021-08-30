class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        

        wordSet = set(words)
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in wordSet and suffix in wordSet:
                    memo[word] = True
                    return True
                if prefix in wordSet and dfs(suffix):
                    memo[word] = True
                    return True
                
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res