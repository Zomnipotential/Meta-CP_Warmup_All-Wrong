import pytest

def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    C = C.replace('A','*')
    C = C.replace('B','A')
    C = C.replace('*','B')
    return C
