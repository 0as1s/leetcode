# encoding=utf-8


def LCS(a, b):
    # 为了让算法的外层循环尽量小，如果a的长度较大，就交换a和b
    if len(a) > len(b):
        a, b = b, a

    total = [0] * len(b)        # 使用total来存放遍历中每个位置上最长序列的长度
    cur = []                    # 使用Cur来存放遍历中若干个位置上的最长序列

    # 初始化a中第一个字母和b比较而产生的total和cur
    i = 0
    for i in range(len(b)):
        if a[0] == b[i]:
            total[i] = 1
            break
        cur.append("")

    for j in range(i, len(b)):
        total[j] = 1
        cur.append(a[0])

    # 为方便在下边的循环中处理第一个位置的值，在total和cur前边各加上一个空的值
    total = [0] + total
    cur = ["", ] + cur

    # 外层循环中用a[i]分别跟b中的字母比较，每次循环更新total和cur
    for i in range(1, len(a)):
        cur_char = a[i]
        temp_total = list(total)  # 保存一个total和cur的复制，用于在a[i]==b[j]时改变值
        temp_cur = list(cur)
        for j in range(0, len(b)):
            # 利用ppt上的规则改变total的值，对应地改变cur的值
            if cur_char == b[j]:
                total[j + 1] = temp_total[j] + 1
                cur[j + 1] = temp_cur[j] + cur_char
            elif total[j] > total[j + 1]:
                cur[j + 1] = cur[j]
                total[j + 1] = total[j]
    print total
    print cur
    print cur[-1], total[-1]


LCS("abcdefgh", "a1b2c3d4e5f6g7h8")
