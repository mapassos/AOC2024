import pytest
import part1
import part2

with open('test.txt') as f:
    data = f.read().split('\n\n')

def test_pt1():
    assert part1.apply_rule(data) == 143

def test_pt2():
    assert part2.apply_rule(data) == 123
