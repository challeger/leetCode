"""
day: 2020-08-30
url: https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
题目名: 实现前缀树
实现一个前缀树,包含insert, search和startsWith这三个操作
示例:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")  return true
    trie.search("app")  return false
    trie.startsWith("app") return true
思路:
    对于前缀树的其中一个节点来说,他应该包括,
        is_str: 从首节点一直到当前节点,是否是一个字符串
        next_chars: 这个节点可以抵达的下一个字符
    对于insert操作,我们只需要每次查找该字符是否已经在当前节点的下一层,不在
    则插入新的节点,否则走到对应的下一个节点即可.当全部插入完后,将当前节点的is_str设置为True

    对于search操作,我们只需要根据字符串的字符,依次查找前缀树中的节点,如果没有找到对应的节点就
    直接返回false,若走到最后一个字符,则返回该节点的is_str.

    对于startWith操作,就只需查找是否有对应的节点即可,不需要考虑是否是字符串.
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {
            'is_str': False,
        }

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.head
        for chr in word:
            if chr not in node:
                node[chr] = {
                    'is_str': False,
                    'next_chars': {}
                }
            node = node[chr]
        node['is_str'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.head
        for chr in word:
            if chr not in node:
                return False
            node = node[chr]
        return node['is_str']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.head
        for chr in prefix:
            if chr not in node:
                return False
            node = node[chr]
        return True


if __name__ == "__main__":
    test = 'apple'
    tree = Trie()
    tree.insert(test)
    print(tree.head)
    print(tree.search('apple'))
    print(tree.search('app'))
    print(tree.startsWith('app'))
    tree.insert('app')
    print(tree.search('app'))
