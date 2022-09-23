import stripe

stripe.api_key = 'sk_test_51LjR1lAwPU6i8NbhG99VH0NpkPpRGs8TTqvOBnmphMs3d07ISjQma1BVLF4TfUo9M2tO2OIxwxqnpdrvBJt48ZUv00XxTqO2zJ'
def test():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'pr_1234',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://dzen.ru/?yredirect=true',
            cancel_url='https://google.com',
        )
    except Exception as e:
        return str(e)
    # return checkout_session 
    print(checkout_session.url)