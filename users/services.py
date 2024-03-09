import stripe

from config.settings import STRIP_SECRET_KEY

stripe_api_key = STRIP_SECRET_KEY


def create_price(payment):
    """ Cоздание продукта и цены """
    stripe.api_key = stripe_api_key
    stripe_product = stripe.Product.create(
        name=payment.paid_course.title
    )

    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=payment.paid_sum*100,
        product_data={"name": stripe_product["name"]},
    )

    print(stripe_price)

    return stripe_price["id"]


def create_stripe_session(stripe_price_id):
    """ создание сессии для получения ссылки на оплату """
    stripe.api_key = stripe_api_key
    stripe_session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{
            'price': stripe_price_id,
            'quantity': 1
        }],
        mode='payment',
    )
    print(stripe_session)
    return stripe_session['url'], stripe_session['id']


def retrieve_stripe_status(payment):
    """ Получение статуса платежа """
    stripe.api_key = stripe_api_key

    stripe_session = stripe.checkout.Session.retrieve(
        payment.payment_id,
    )

    return stripe_session["status"]

