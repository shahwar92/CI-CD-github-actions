"""Unit tests for math utility functions in src/math_utils.py."""

import pytest
from src.math_utils import add, divide, is_even, multiply, subtract


class TestAdd:
    """Tests for the add() function."""

    def test_positive_numbers(self):
        """Test addition of two positive integers."""
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        """Test addition of two negative integers."""
        assert add(-1, -4) == -5

    def test_mixed_sign(self):
        """Test addition of a negative and a positive integer."""
        assert add(-3, 7) == 4

    def test_floats(self):
        """Test addition of floating-point numbers."""
        assert add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtract:
    """Tests for the subtract() function."""

    def test_basic(self):
        """Test subtraction of two positive integers."""
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        """Test subtraction resulting in a negative value."""
        assert subtract(3, 8) == -5


class TestMultiply:
    """Tests for the multiply() function."""

    def test_positive(self):
        """Test multiplication of two positive integers."""
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(99, 0) == 0

    def test_floats(self):
        """Test multiplication with floating-point numbers."""
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    """Tests for the divide() function."""

    def test_exact_division(self):
        """Test division resulting in an integer."""
        assert divide(10, 2) == 5

    def test_float_result(self):
        """Test division resulting in a float."""
        assert divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero_raises(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(5, 0)


class TestIsEven:
    """Tests for the is_even() function."""

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, True),
            (2, True),
            (4, True),
            (1, False),
            (7, False),
            (-2, True),
            (-3, False),
        ],
    )
    def test_various_inputs(self, n, expected):
        """Test is_even() with multiple integer inputs."""
        assert is_even(n) == expected
