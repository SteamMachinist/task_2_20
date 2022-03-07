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


def items_in_task_order(m: list):
    row_count, col_count = len(m), len(m[0])
    to_right = True
    for row in range(row_count):
        if to_right:
            current_range = range(col_count)
        else:
            current_range = range(col_count - 1, -1, -1)
        to_right = not to_right
        for column in current_range:
            yield m[row][column]


def pairs_of_neighbors(iterable: iter):
    first = True
    for v in iterable:
        if first:
            first = False
        else:
            yield prev, v
        prev = v


def check(m: list, ordering):
    return all((p[1] - p[0]) * ordering > 0 for p in pairs_of_neighbors(items_in_task_order(m)))


if __name__ == '__main__':
    matrix = read_matrix_from_file("input/input2.txt")
    write_matrix_to_file("output/output2.txt",
                         matrix,
                         check(matrix, (matrix[0][1] - matrix[0][0])))
