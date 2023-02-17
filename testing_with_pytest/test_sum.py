import pytest

from sum import sum_numbers

@pytest.fixture(scope="function")
def connection():
    conn = {'status': 'connected'}
    yield conn
    # Do something after the test is executed


class TestSumNumbers:

    def test_for_two_positive_numbers(self):
        result = sum_numbers(2, 3)
        assert result == 5


    @pytest.mark.parametrize("a, b, expected", [(-2, -3, 0), (-2, 3, 1), (2, -3, -1)])
    def test_for_two_negatives(self, a, b, expected, connection):
        """
        Test if function returns 0 if two negative numbers are passed as arguments!
        """
        result = sum_numbers(a, b)
        assert result == expected