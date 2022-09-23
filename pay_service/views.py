from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers.ItemSerializer import ItemSerializer
from .models import Item
# import stripe
from rest_framework.parsers import JSONParser
from .bussines_logic import create_items_list, stripe_create_session


@csrf_exempt
def bay_items(requests):
    """
    Купить сразу несколько вещей.
    В POST  запросе передаётся список вещей.
    Возвращает номер сессии и адрес страницы оплаты.
    """
    data = JSONParser().parse(requests)
    items_list = create_items_list(data)
    if items_list == False:
        return JsonResponse({'error':'ошибка данных'})
    session = stripe_create_session(items_list)
    return JsonResponse(session)


def bay(requests, id):
    """
    Купить вещь по номеру id.
    В качестве параметра передаётся id вещи.
    Возвращает номер сессии и адрес страницы оплаты.
    """
    item = create_items_list(id)
    if item == False:
        return JsonResponse({'error':'ошибка данных'})
    session = stripe_create_session(item)
    return JsonResponse(session)
    

def item(requests, id):
    """
    Возвращает вешь по номеру id
    """
    try:
        item = Item.objects.get(id_item=id)
    except:
        return JsonResponse({'error':'Не найден товар'})
    serializer = ItemSerializer(item)
    return  JsonResponse(serializer.data)  
   

def get_all_items(requests):
    """
    Возвращает список всех вещей в базе.
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)
