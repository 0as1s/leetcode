# encoding=utf-8

matrix_shapes = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]


def calculate_path(matrix_shapes):
    # sums[i,j]存放从Ai连乘到Aj的最小用时
    sums = [[0 for i in range(len(matrix_shapes))]
            for j in range(len(matrix_shapes))]
    # c[j,j]存放从Ai连乘到Aj时，中间从哪个位置切开
    c = [[0 for i in range(len(matrix_shapes))]
         for j in range(len(matrix_shapes))]
    # 初始化Ai×A（i+1）需要的乘法数
    for i in range(len(matrix_shapes) - 1):
        sums[i][i + 1] = matrix_shapes[i][0] * \
            matrix_shapes[i][1] * matrix_shapes[i + 1][1]
    # i表示连乘的长度，每个循环都计算Aj×...×A(j+i)需要的乘法数
    for i in range(2, len(matrix_shapes)):
        # j表示连乘起始的位置
        for j in range(len(matrix_shapes) - i):
            min_ = float("Inf")
            # ｋ表示切开的位置，在ｊ到ｊ＋ｉ之间寻找ｋ时，更新ｓｕｍｓ矩阵和ｃ矩阵
            for k in range(j, j + i):
                sum_ = sums[j][k] + matrix_shapes[j][0] * matrix_shapes[
                    k][1] * matrix_shapes[j + i][1] + sums[k + 1][j + i]
                if sum_ < min_:
                    min_ = sum_
                    sums[j][j + i] = min_
                    c[j][j + i] = k
    print sums
    print c                     # 下标是从０开始的，所以和ｐｐｔ上的ｃ矩阵有不同
    return c


# 递归调用build_str来生成连乘的路径
# ｃ是上一个函数算出的ｃ矩阵，ｉ，ｊ表示当前在ｃ中的位置
# left默认为true, 表示当前结果在乘号左边，直接输出即可，不用加括号，否则要加括号
def build_str(c, i, j, left=True):
    # 如果当前只有一个矩阵或两个矩阵已经相邻，中间没有可以切分的点，就直输出，否则递归调用
    if i == j:
        return "A%d" % (i + 1)
    elif j - i == 1:
        content = "A%d*A%d" % (i + 1, j + 1)
    else:
        content = build_str(c, i, c[i][j]) + "*" + build_str(
            c, c[i][j] + 1, j, False)
    if not left:
        return "(" + content + ")"
    return content


c = calculate_path(matrix_shapes)
print build_str(c, 0, len(matrix_shapes) - 1)
