def apply_discount(total_price):
    """
    Прилага отстъпка според общата цена.
    """
    if total_price > 1000:
        return total_price * 0.90  # 10% отстъпка
    elif total_price > 500:
        return total_price * 0.95  # 5% отстъпка
    return total_price
