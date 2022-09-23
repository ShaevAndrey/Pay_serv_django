import os
import copy
import stripe
from django.conf import settings
from .models import Item


stripe.api_key = settings.STRIPE_KEY

def create_items_list(items):
    """
    Принимает на вход либо id вещи, либо список покупки.
    Возвращает список, отформатированный для запроса stripe.
    """
    result_list = list()
    result_item = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': 0,
                'product_data': {
                    'name': '',
                },
            },
            'quantity': 1,
        }

    if isinstance(items, int):
        try:
            item_request = Item.objects.get(id_item = items)
        except:
            return False
        result_item['price_data']['unit_amount'] = item_request.price
        result_item['price_data']['product_data']['name'] = item_request.name
        return [result_item]
    
    if len(items) == 0:
        return False
    for item in items:
        try:
            item_request = Item.objects.get(id_item = item['id_item'])
        except:
            return False
        current_item = copy.deepcopy(result_item)
        current_item['price_data']['unit_amount'] = item_request.price
        current_item['price_data']['product_data']['name'] = item_request.name
        current_item['quantity'] = item['count']
        result_list.append(current_item)
    return result_list

        

def stripe_create_session(items):
    """
    Принимает на вход отформатированный список вещей.
    Возвращает id сессии и ссылку на оплату.
    """
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=items,
            mode='payment',
            success_url='https://shaevandrey.github.io/Pay_service_front/success',
            cancel_url='https://shaevandrey.github.io/Pay_service_front/error',
        )
    except Exception as e:
        return {'error':'ошибка оплаты'}
    return {"session":checkout_session.id, 'url':checkout_session.url}