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


def is_matrix_ordered_sequence(m: list):
    return True


if __name__ == '__main__':
    matrix = read_matrix_from_file("input/input1.txt")
    write_matrix_to_file("output/output1.txt",
                         matrix,
                         is_matrix_ordered_sequence(matrix))
