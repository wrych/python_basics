import scripts.multiply_by_2


def test_multiplying_by_2(val= 5 ):
    output = scripts.multiply_by_2.multiply_by_2(5)
    assert output == 10