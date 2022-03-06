# (*) Для переданного двумерного массива определить, образуют ли его элементы упорядоченную последовательность при
# просмотре элементов в следующем порядке:

def read_matrix_from_file(filepath):
    file = open(filepath, 'r')
    m = []
    for row in file:
        m.append([int(x) for x in row.strip().split(" ")])
    file.close()
    return m


def write_matrix_to_file(filepath, m: list, is_ordered: bool):
    file = open(filepath, 'w')
    for row in m:
        file.write(" ".join([str(x) for x in row]))
        file.write("\n")
    file.write("\nSequence is")
    if not is_ordered:
        file.write(" not")
    file.write(" ordered")
    file.close()


def is_element_ordered(m: list, row_n: int, column_n: int, seq_order: int, to_right: bool):
    if row_n == len(m) - 1 and column_n == len(m[row_n]) - 1:
        return True
    if to_right:
        if column_n == len(m[row_n]) - 1:
            if (m[row_n + 1][column_n] - m[row_n][column_n]) * seq_order < 0:
                return False
        else:
            if (m[row_n][column_n + 1] - m[row_n][column_n]) * seq_order < 0:
                return False
    else:
        if column_n == 0:
            if (m[row_n + 1][column_n] - m[row_n][column_n]) * seq_order < 0:
                return False
        else:
            if (m[row_n][column_n - 1] - m[row_n][column_n]) * seq_order < 0:
                return False
    return True


def is_row_ordered(m: list, row_n: int, seq_order: int, to_right: bool, row_range: range):
    for column_n in row_range:
        if not is_element_ordered(m, row_n, column_n, seq_order, to_right):
            return False
    return True


def is_matrix_ordered(m: list):
    seq_order = (m[0][1] - m[0][0]) / abs(m[0][1] - m[0][0])
    to_right = True
    for row_n in range(len(m)):
        if to_right:
            if not is_row_ordered(m, row_n, seq_order, to_right, range(len(m[row_n]))):
                return False
        else:
            if not is_row_ordered(m, row_n, seq_order, to_right, range(len(m[row_n]) - 1, -1, -1)):
                return False
        to_right = not to_right
    return True


if __name__ == '__main__':
    matrix = read_matrix_from_file("input/input2.txt")
    write_matrix_to_file("output/output2.txt",
                         matrix,
                         is_matrix_ordered(matrix))
