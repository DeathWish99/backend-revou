import pytest

def inc(x):
    return x+1

def test_example():
    assert inc(3) == 4