from sum import sum_numbers

def test_sum_numbers_function():
    """
    Test a function that sums two numbers.
    """
    result = sum_numbers(2, 3)
    if result == 5:
        print('Test Passed!')
    else:
        print('Test Failed! To input a = 2, b = 3')


def test_sum_functions_called_with_at_least_one_negative_numbers_must_return_0():
    result = sum_numbers(-1, -3)
    if result == 0:
        print("Test Passed!")
    else:
        print("Test Failed! To input a = -1 and b = -3")

    result = sum_numbers(4, -5)
    if result == 0:
        print("Test Passed!")
    else:
        print("Test Failed! To Input a = 4 and b = -5")

    result = sum_numbers(-4, 5)
    if result == 0:
        print("Test Passed!")
    else:
        print("Test Failed! To Input a = -4 and b = 5")


if __name__ == '__main__': 
    test_sum_numbers_function()
    test_sum_functions_called_with_at_least_one_negative_numbers_must_return_0()