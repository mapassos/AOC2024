import pytest
import part1

with open('test.txt') as f:
    data = f.read()

def test_pt1():
    assert part1.count_distinct_pos(data) == 41
