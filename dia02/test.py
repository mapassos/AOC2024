import pytest
import part1
import part2

with open('test.txt') as f:
    data = f.read()

def test_pt1():
    assert part1.count_safe_reports(data) == 2

def test_pt2():
    assert part2.count_safe_reports(data) == 4
