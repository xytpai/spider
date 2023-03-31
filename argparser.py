import argparse


def parse():
    parser = argparse.ArgumentParser(description='Spider')
    parser.add_argument('--dir', type=str, default='./output')
    parser.add_argument('--depth', type=int, default=1000)
    args = parser.parse_args()
    return args
