"""
day: 2020-09-02
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdu2v2/
题目名: 实现Trie(前缀树)
实现一个前缀树,包含insert,search和statsWith三个操作

复习.
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {
            'is_str': False
        }

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.head
        for char in word:
            if char not in temp.keys():
                temp[char] = {
                    'is_str': False
                }
            temp = temp[char]
        temp['is_str'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.head
        for char in word:
            if char not in temp:
                return False
            temp = temp[char]
        return temp['is_str']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.head
        for char in prefix:
            if char not in temp:
                return False
            temp = temp[char]
        return True


if __name__ == "__main__":
    tree = Trie()
    tree.insert('apple')
    print(tree.head)
    print(tree.search('apple'))
    print(tree.search('app'))
    print(tree.startsWith('app'))
