def calculate_subtotal(price, quantity):
    """Calculate the total cost of products before discount."""
    if price <= 0:
        raise ValueError("Price must be greater than 0")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return price * quantity


def calculate_discount(subtotal, discount_percent):
    """Calculate discount amount based on subtotal and percentage."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    if not 0 <= discount_percent <= 50:
        raise ValueError("Discount must be between 0 and 50")

    return subtotal * discount_percent / 100


def calculate_total(subtotal, discount):
    """Calculate final order total after discount."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    if discount < 0:
        raise ValueError("Discount cannot be negative")

    if discount > subtotal:
        raise ValueError("Discount cannot be greater than subtotal")

    return subtotal - discount


def create_order(price, quantity, discount_percent):
    """Create an order and return all calculated values."""
    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal, discount_percent)
    total = calculate_total(subtotal, discount)

    return {
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "discount_percent": discount_percent,
        "discount": discount,
        "total": total,
    }
