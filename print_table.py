#!/usr/bin/env python2.7


def print_table(rows):
    """
    +---------------+------------------------------+---------------+
    |title 0        | title 1                      | title 2       |
    +---------------+------------------------------+---------------+
    |row 0 column 0 | row 0 column 1 which is long | row 0 column 2|
    |row 1 column 0 | row 1 column 1               | row 1 column 2|
    +---------------+------------------------------+---------------+
    """
    # calculate column widths
    widths = [len(max(columns, key=len)) for columns in zip(*rows)]

    # print open seperator line
    print('+' + '-+-'.join('-' * width for width in widths) + '+')

    # print header
    header, data = rows[0], rows[1:]
    print('|' + ' | '.join(format(title, "%ds" % width) for width, title in zip(widths, header)) + '|')
    # print seperator line
    print('+' + '-+-'.join('-' * width for width in widths) + '+')

    # print real data
    for row in data:
        print('|' + " | ".join(format(cdata, "%ds" % width) for width, cdata in zip(widths, row)) + '|')
    # print close seperator line
    print('+' + '-+-'.join('-' * width for width in widths) + '+')

if __name__ == "__main__":
    l = [['title 0', 'title 1', 'title 2'], ['row 0 column 0', 'row 0 column 1 which is long', 'row 0 column 2'], ['row 1 column 0', 'row 1 column 1', 'row 1 column 2']]
    print_table(l)
