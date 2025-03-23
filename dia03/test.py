import pytest
import part1
import part2

with open('test.txt') as f:
    data = f.read()

def test_pt1():
    assert part1.get_res(data) == 161

def test_pt2():
    assert part2.get_res(data) == 161
