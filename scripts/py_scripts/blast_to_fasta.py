import sys


def read_file(f_name):
    seq_data = {}

    with open(f_name, "r") as file:

        for line in file:
            curr_seq = line.rsplit()

            if len(curr_seq) > 0:
                if curr_seq[0] in seq_data:
                    seq_data[curr_seq[0]] += curr_seq[2]
                else:
                    seq_data[curr_seq[0]] = curr_seq[2]
    return seq_data


def main():
    if 1 >= len(sys.argv):
        print('Please input blast query output!')
    else:
        query_file = sys.argv[1]
        seq_data = read_file(query_file)

        for i in seq_data:
            print(f'>{i}\n{seq_data[i]}', '\n')


if __name__ == '__main__':
    main()


