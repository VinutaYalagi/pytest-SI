from si import simpleInt
def test_calculate_SI():
    assert simpleInt(1000,4,2) == 80

def test_calculate_zero():
    assert simpleInt(1000,0,2) == 0