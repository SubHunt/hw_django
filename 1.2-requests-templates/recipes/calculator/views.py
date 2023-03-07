from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    return render(request, 'calculator/index.html')


def dishes(request, dish):
    qty = int(request.GET.get('servings', 1))
    dish_ready = DATA[dish]
    dish_make = {}
    for k, v in dish_ready.items():
        dish_make[k] = v * qty
    context = {
        'recipe': dish_make,
        'qty': qty,
    }
    return render(request, 'calculator/dishes.html', context)


def pasta(request):
    return dishes(request, 'pasta')


def omlet(request):
    return dishes(request, 'omlet')


def buter(request):
    return dishes(request, 'buter')
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
