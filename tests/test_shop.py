import pytest

from shop import (
    calculate_discount,
    calculate_subtotal,
    calculate_total,
    create_order,
)


def test_calculate_subtotal():
    result = calculate_subtotal(500, 2)

    assert result == 1000
    assert isinstance(result, int)
    assert result > 0


def test_calculate_subtotal_with_other_values():
    result = calculate_subtotal(125.5, 4)

    assert result == 502.0
    assert isinstance(result, float)
    assert result > 0


def test_calculate_subtotal_invalid_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_subtotal(0, 2)

    assert isinstance(exc_info.value, ValueError)
    assert str(exc_info.value) == "Price must be greater than 0"


def test_calculate_subtotal_invalid_quantity():
    with pytest.raises(ValueError) as exc_info:
        calculate_subtotal(500, 0)

    assert isinstance(exc_info.value, ValueError)
    assert str(exc_info.value) == "Quantity must be greater than 0"


def test_calculate_discount():
    result = calculate_discount(1000, 20)

    assert result == 200
    assert isinstance(result, float)

    # Boundary value: maximum allowed discount
    max_discount = calculate_discount(1000, 50)

    assert max_discount == 500
    assert isinstance(max_discount, float)


def test_calculate_discount_invalid_percent():
    with pytest.raises(ValueError) as exc_info:
        calculate_discount(1000, 51)

    assert isinstance(exc_info.value, ValueError)
    assert str(exc_info.value) == "Discount must be between 0 and 50"


def test_calculate_total_invalid_discount():
    with pytest.raises(ValueError) as exc_info:
        calculate_total(1000, 1500)

    assert isinstance(exc_info.value, ValueError)
    assert str(exc_info.value) == "Discount cannot be greater than subtotal"


def test_create_order():
    order = create_order(500, 4, 10)

    assert isinstance(order, dict)
    assert order["price"] == 500
    assert order["quantity"] == 4
    assert order["subtotal"] == 2000
    assert order["discount_percent"] == 10
    assert order["discount"] == 200
    assert order["total"] == 1800

