def add(a, b):
    return a + b

# run all test:
# 1. Перейти в terminal
# 2. Набрать команду: pytest

def test_add():
    assert add(1, 2) != 4
    assert add(2, 2) == 4