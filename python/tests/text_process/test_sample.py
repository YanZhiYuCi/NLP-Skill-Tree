import pytest


# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def test_answer_v1():
    assert inc(3) == 4


if __name__ == '__main__':
    # 另一种启动方法是直接在命令行中输入pytest
    pytest.main()
