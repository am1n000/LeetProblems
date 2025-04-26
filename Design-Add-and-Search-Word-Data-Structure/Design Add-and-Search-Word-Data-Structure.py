class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["*"] = None

    def search(self, word: str) -> bool:

        def dfs(j, root):
            if not root:
                return False
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur:
                        return False
                    cur = cur[c]
            if "*" in cur:
                return True
            return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)