from collections import Counter
def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1)!=len(word2):
            return bool(0)
        
        hashmap1 = Counter(list(word1))
        hashmap2 = Counter(list(word2))

        return ((sorted(hashmap1.keys())==sorted(hashmap2.keys()))and(sorted(hashmap1.values())==sorted(hashmap2.values())))