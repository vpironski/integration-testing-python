# test_integration.py

import pytest
from product_module import add_product
from order_module import calculate_total_price

# Фикстура за настройка на тестовите данни
@pytest.fixture
def setup_products():
    add_product(1, "Laptop", 1200)
    add_product(2, "Mouse", 20)

# Тест 1: Поръчка без отстъпка
def test_order_without_discount(setup_products):
    order_items = [(2, 3)]  # 3x Mouse (20 * 3 = 60)
    total_price = calculate_total_price(order_items)
    assert total_price == 60  # Без отстъпка

# Тест 2: Поръчка с няколко продукта
def test_order_with_multiple_products(setup_products):
    order_items = [(1, 1), (2, 2)]  # 1x Laptop (1200) + 2x Mouse (20 * 2 = 40) = 1240
    total_price = calculate_total_price(order_items)
    expected_price = 1240 * 0.9  # 10% отстъпка -> 1240 * 0.9 = 1116
    assert total_price == expected_price

# Тест 3: Поръчка с несъществуващ продукт
def test_order_with_invalid_product(setup_products):
    order_items = [(99, 1)]  # Несъществуващ продукт
    total_price = calculate_total_price(order_items)
    assert total_price == 0  # Няма такъв продукт, цената е 0

# Тест 4: Поръчка с отстъпка 5%
def test_order_with_five_percent_discount(setup_products):
    order_items = [(1, 1)]  # 1x Laptop (1200), но с 10% отстъпка -> 1200 * 0.9 = 1080
    total_price = calculate_total_price(order_items)
    assert total_price == 1080