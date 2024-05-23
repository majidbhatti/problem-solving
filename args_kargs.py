from datetime import datetime
from datetime import timedelta
from loguru import logger


def test_args(*args):
    print('into the args function')
    return sum([s for s in args])


def test_kargs(**kargs):
    print('into the k-args function')
    for k, v in kargs.items():
        print(f'key is:{k}, and value:{v}')


def test_non_and_kargs(a, b, **kargs):
    print('into actual test function')
    print('a is:', a, 'b is:', b)
    for k, v in kargs.items():
        print(f'key is:{k}, value:{v}')


if __name__ == '__main__':
    alert = {'generatedAt': '2024-02-13T13:25:26.547316Z'}
    x = [alert, {'generatedAt': '2024-03-13T13:25:26.547316Z'}]
