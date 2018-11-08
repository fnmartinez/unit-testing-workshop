import argparse

import calc


def get_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('operand',
                        choices=['add', 'subtract', 'multiply', 'divide'])
    parser.add_argument('a', type=int)
    parser.add_argument('b', type=int)
    return parser.parse_args(args)


if __name__ == '__main__':
    args = get_args()
    if args.operand == 'add':
        print(calc.add(args.a, args.b))
    elif args.operand == 'subtract':
        print(calc.subtract(args.a, args.b))
    elif args.operand == 'multiply':
        print(calc.multiply(args.a, args.b))
    elif args.operand == 'divide':
        print(calc.divide(args.a, args.b))
