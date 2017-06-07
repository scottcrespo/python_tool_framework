import sys
import argparse
import typing
from core.framework import Framework

def get_args():
    parser = argparse.ArgumentParser(description='It is a parser')
    parser.add_argument(
                        '--env',
                        dest='env',
                        type=str,
                        default='local',
                        )

    return parser.parse_args()

if __name__ == '__main__':
    print (sys.argv[0])
    args = get_args()
    cloee_mongo = Framework(args.env)
