"""
day: 2020-09-08
url: https://leetcode-cn.com/problems/encode-and-decode-tinyurl/
题目名: TinyURL的加密与解密
TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.

要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的
你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
思路:
定义一个由数字大写字母小写字母组成的字符串,每次保存时随机从字符串中取6个字符,作为字典的键保存在类中,并返回该key.
解密时只需要用这个key去字典中取值即可.
"""
import random


class Codec:
    _codeMap = dict()
    _chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZMXNCBV'

    @classmethod
    def getRandom(cls):
        return ''.join(random.sample(cls._chars, 6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getRandom()
        while key in self._codeMap:
            key = self.getRandom()
        self._codeMap[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl[-6:]
        return self._codeMap[key]
