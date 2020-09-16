
import numpy as np
from itertools import combinations


def main(list_input, time_interval=4):
    assert time_interval != 0
    sum_max = -1
    best_list = None
    print(len(list_input), list_input)
    for num in range(1, int(24/time_interval)):
        for tmp in combinations(list_input, num):
            if check_legal(tmp, time_interval):
                sum_tmp = get_sum(tmp)
                if sum_tmp > sum_max:
                    best_list = tmp
                    sum_max = sum_tmp
    return best_list, sum_max


def dp_simple(list_input):
    acc_ctr = [tmp[1] for tmp in list_input]
    time = [tmp[0] for tmp in list_input]
    ctr = [tmp[1] for tmp in list_input]
    for i in range(0, 10):
        for j in range(i + 1, 10):
            if time[j] - time[i] >= 4:
                acc_ctr[j] = max(acc_ctr[i] + ctr[j], acc_ctr[j])
    print(acc_ctr)
    return max(acc_ctr)


def check_legal(list_input_check, threshold):
    for i in range(len(list_input_check) - 1):
        if (list_input_check[i + 1][0] - list_input_check[i][0]) < threshold:
            return False
    return True


def get_sum(list_input):
    return np.sum([tmp[1] for tmp in list_input])


def test_from_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return lines


def test():
    list_input = []
    list_input.append([8, 0.4])
    list_input.append([9, 0.5])
    list_input.append([10, 0.6])
    list_input.append([12, 0.2])
    list_input.append([13, 0.2])
    list_input.append([15, 0.1])
    list_input.append([15.3, 0.5])
    list_input.append([15.5, 0.6])
    list_input.append([20, 0.2])
    list_input.append([22, 0.2])
    print(main(list_input))
    print(dp_simple(list_input))


if __name__ == '__main__':
    test()
