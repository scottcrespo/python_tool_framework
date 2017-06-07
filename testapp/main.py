import os
import sys
import argparse
import typing
# must add path of parent project so we can import core module
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
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
    cloee_mongo = Framework(args.env, app="testapp")
    print (cloee_mongo.config.FOO)
    print (cloee_mongo.config.MYFOO)
    print (cloee_mongo.config.MYDICT)
