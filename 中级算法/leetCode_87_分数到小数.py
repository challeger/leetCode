"""
day: 2020-08-23
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xwm8ne/
题目名: 分数到小数
题目描述: 给定两个整数,分别表示分数的分子numerator和分母denominator,以字符串形式返回小数
示例:
    输入: numerator = 1, denominator = 2
    输出: "0.5"
    输入: numerator = 2, denominator = 1
    输出: "2"
    输入: numerator = 2, denominator = 3
    输出: "0.(6)"
思路:
    如果小数部分有循环,那么循环开始时的余数必然在之前出现过一次
    以此为依据来判断是否进入了循环.
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not test1:
            return '0'
        res = []
        # 判断正负
        if numerator > 0 ^ denominator > 0:
            res.append('-')
        # 将绝对值进行整除与求余
        int_num, foo = divmod(abs(numerator), abs(denominator))
        # 整数部分直接添加到结果中
        res.append(str(int_num))
        # 判断是否要求小数
        if foo:
            # 添加小数点
            res.append('.')
            # 用来记录余数出现的位置
            hashmap = {}
            while foo:
                # 如果出现了重复的余数,那么说明进入了循环
                if foo in hashmap:
                    # 在余数第一次出现的位置前方插入(
                    res.insert(hashmap[foo], '(')
                    # 在最后添加)
                    res.append(')')
                    break
                # 否则记录余数出现的位置
                hashmap[foo] = len(res)
                foo *= 10
                # 计算该位除后的结果
                res.append(str(foo // denominator))
                # 计算下一位
                foo %= denominator
        return ''.join(res)


if __name__ == "__main__":
    test1 = 1
    test2 = 3
    s = Solution()
    print(s.fractionToDecimal(test1, test2))
