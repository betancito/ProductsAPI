def sum(a: int, b: int) -> int:
    return a+b
def sub(a: int, b: int) -> int:
    return a-b
def mult(a: int, b: int) -> int:
    return a*b
def div(a: int, b: int) -> int:
    return a/b

#test
def test_sum() -> None:
    assert sum(1,2) == 3
def test_sub() -> None:
    assert sub(1,2) == -1
def test_mult() -> None:
    assert mult(1,2) == 2
def test_div() -> None:
    assert div(1,2) == 0.5
    
    
    