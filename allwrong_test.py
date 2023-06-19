import pytest
import allwrong as aw

def test_getWrongAnswers(inputn, inputc, output):
    assert aw.getWrongAnswers(inputn, inputc) == output

test_getWrongAnswers(2, 'ABA', 'BAB')
test_getWrongAnswers(2, 'BBBBB', 'AAAAA')
