from src.vector import Vector

def test_make_vector():
    v = Vector([1,2,3,4])

    assert v.dims == 4

def test_norm():
    v = Vector([3,4])
    assert v.norm == 7