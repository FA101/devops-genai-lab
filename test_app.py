from app import calculate_order_total, calculate_shipping


def test_calculate_shipping():
    # 10 kg * 1.5 + 100 km * 0.1 + 5.0 de taxa = 30.0
    assert calculate_shipping(10, 100) == 30.0


def test_calculate_order_total():
    assert calculate_order_total(200, 10, 100) == 230.0
