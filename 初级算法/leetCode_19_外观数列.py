"""
day: 2020-08-12
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnpvdm/
题目名: 外观数列
题目描述: 给定一个正整数n in range(1, 31), 输出外观数列的第n项, 每一项以字符串表示
[外观数列], 从数字1开始, 序列的每一项都是对前一项的描述, 前五项如下:
1.  1           # 第一项是数字1
2.  11          # 前一项是1个1,记作11
3.  21          # 前一项是2个1,记作21
4.  1211        # 前一项是1个2 1个1,记作1211
5.  111221      # 前一项是1个1 1个2 2个1,记作111221
示例:
    输入: 1
    输出: '1'

    输入: 4
    输出: '1211'
思路:
    用输入4来举例
    应该循环3次,
    每次循环都遍历result
    每当 当前的数字不等于下一位数字,或者指针的位置i + 当前数字出现的次数count>=len(result)时,
    将str(count)与result[i]拼接到一个临时字符串中,每次遍历完成将这个临时字符串赋给result.

    第一次循环开始:
    result = '1', foo = '', count = 1, i = 0, len(result) = 1

    遍历字符串开始:
    i + count >= 1 -> foo += str(1) + 1 -> foo = '11', count = 1
    遍历字符串完成.

    第二次循环开始:
    result = '11', foo = '', count = 1, i = 0, len(result) = 2

    遍历字符串开始:
    i = 0, count = 1, result[i] = 1, result[i+1] = 1
    -> count = count + 1

    i = 1, count = 2 -> i + count >= 2 -> foo += str(2) + '1', count = 1
    遍历字符串完成

    第三次循环开始:
    result = '21', foo = '', count = 1, i = 0, len(result) = 2

    遍历字符串开始:
    i = 0, count = 1, result[i] = 2, result[i+1] = 1, result[i] != result[i+1]
    -> foo += str(1) + '2' --> foo = '12', count = 1

    i = 1, count = 1 -> i + count >= 2
    -> foo += str(1) + '1' --> foo = '1211'
    遍历字符串完成
    result = foo = '1211'
    最终返回结果'1211'
"""


class Solution:
    @staticmethod
    def countAndSay(n: int) -> str:
        result = '1'
        for _ in range(1, n):
            foo, count = '', 1
            for i in range(len(result)):
                if i + count >= len(result) or result[i] != result[i+1]:
                    foo += str(count) + result[i]
                    count = 1
                else:
                    count += 1
            result = foo
        return result


if __name__ == "__main__":
    test = 4
    print(Solution.countAndSay(test))
