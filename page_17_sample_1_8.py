# @Time    : 2019/10/11 22:42
# @Author  : REN Hao
# @FileName: page_17_sample_1_8.py
# @Software: PyCharm

from numpy import mat
from numpy.linalg import solve

if __name__ == "__main__":
    # SS + SF = 2/3
    # SS + FS = 1/2
    # SS + SF + FS = 3/4
    # SS + SF + FS + FF = 1

    # 系数矩阵
    a = mat([[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]])

    # 常数项列矩阵
    b = mat([2.0/3.0, 0.5, 0.75, 1.0]).T

    # 方程组的解
    SS, SF, FS, FF = solve(a, b)

    # 只有一個團隊完成任務的概率為SF+FS
    one_success = float(SF[0])+float(FS[0])

    # 在只有一个团队完成任务的情况下N完成任务的概率为
    ratio_N_success = float(FS)/one_success
    print(ratio_N_success)
