import pytest
import part1
import part2

with open('test.txt') as f:
    tab = f.read().split()

def test_pt1():
    search = part1.SearchWords(tab)
    assert search.searchncount('XMAS') == 18

def test_pt2():
    search = part2.SearchWords(tab)
    assert search.searchncount() == 9
