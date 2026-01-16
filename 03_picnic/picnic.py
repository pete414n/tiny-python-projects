#!/usr/bin/env python3

import argparse

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic -- List the items to bring",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        nargs='+',
                        metavar='str',
                        help='Item(s) to bring')

    parser.add_argument('-s', '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()

def main():

    args = get_args()
    items = args.item

    if args.sorted:
        items.sort()

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print(f'You are bringing {bringing}.')

if __name__ == '__main__':
    main()