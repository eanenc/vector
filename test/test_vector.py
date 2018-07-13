from src.vector import Vector

def test_make_vector():
    v = Vector([1,2,3,4])

    assert v.dims == 4

def test_norm():
    v = Vector([3,4])
    assert v.norm == 5

def test_unit_vector():
    v = Vector ([5,3,1,9,2])
    assert v.unit_vector().norm ==1   

def test_scaling_vector():
    v = Vector ([1,2,3])
    v1 = Vector ([3,6,9])
    
    assert v.scale_vector(3) == Vector ([3,6,9])

    #assert __eq(v,v1)