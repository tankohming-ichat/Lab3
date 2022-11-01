import Lab3
import Lab2.bmi as bmi

print("Test_bmi")


def test_bmi_under_weight():
    result = []
    height = 1.6
    weight = 40
    result = bmi.calculate_bmi(height, weight)

    assert (result == -1)

def test_bmi_normal_weight():
    result = []
    height = 1.6
    weight = 55
    result = bmi.calculate_bmi(height, weight)

    assert (result == 0)

def test_bmi_over_weight():
    result = []
    height = 1.6
    weight = 80
    result = bmi.calculate_bmi(height, weight)

    assert (result == 1)