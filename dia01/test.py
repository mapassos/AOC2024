import pt12
import pytest

with open('test.txt') as f:
    file = f.read()

data_parsed = pt12.data_parser(file)

def test_pt1():
    assert pt12.total_dist(*data_parsed) == 11

def test_pt2():
    assert pt12.similarity_score(*data_parsed) == 31

