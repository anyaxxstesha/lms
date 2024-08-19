import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def get_or_create_stripe_product(obj):
    """Get or create a stripe product"""
    if product := stripe.Product.retrieve(str(obj.pk)):
        return product
    return stripe.Product.create(
        id=str(obj.pk),
        name=obj.title,
        description=obj.description,
    )


def create_stripe_price(amount, product: stripe.Product):
    """Создает цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product.id
    )


def create_stripe_session(price):
    """Создает сессию в страйпе"""

    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.0:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
