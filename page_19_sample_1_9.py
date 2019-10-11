# @Time    : 2019/10/11 22:43
# @Author  : REN Hao
# @FileName: page_19_sample_1_9.py
# @Software: PyCharm

if __name__ == "__main__":
    print("例1.9")
    # P(雷达报警|飞机出现) = 0.99
    p_warning_if_plain = 0.99

    # P(雷达未报警|飞机出现) = 1 - P(雷达报警|飞机出现)
    p_not_warning_if_plain = 1 - p_warning_if_plain

    # P(雷达报警|飞机未出现) = 0.1
    p_warning_if_not_plain = 0.1

    # P(飞机出现) = 0.05
    p_plain = 0.05

    # P(飞机未出现)的概率
    p_not_plain = 1 - p_plain

    # P(雷达报警且飞机未出现) = P(雷达报警|飞机未出现) * P(飞机未出现)
    p_not_plain_and_warning = p_warning_if_not_plain * p_not_plain
    print("飞机没有出现在该地区而雷达虚假报警的概率为%s" % str(p_not_plain_and_warning))

    # P(雷达未报警且飞机出现) = P(雷达未报警|飞机出现) * P(飞机出现)
    p_plain_and_not_warning = p_not_warning_if_plain * p_plain
    print("飞机出现在该地区而雷达没有探测到的概率有%s" % p_plain_and_not_warning)
