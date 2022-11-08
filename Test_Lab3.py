import Lab3
import Lab2.Lab2 as Lab2

print("Test_Lab3")


def test_REQ_02():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 60, 30, 23, 23]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)

def test_REQ_03():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 2)

def test_REQ_04():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 0)

def test_REQ_05():
    input_arr = [64, 34, 25, 12, 22, 11, 90.3, 60, 30, 23]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 3)
def test_min_max():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_min_max(input_arr)
    test_result = [1,10]
    assert (result == test_result)
def test_calc_average():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_average(input_arr)
    test_result = 5.5
    assert (result == test_result)
def test_calc_median_temp():
    input_arr = [1,2,3,4,5,6,7,8,9,10]
    result = Lab2.calc_median_temperature(input_arr)
    test_result = 5.5
    assert (result == test_result)
