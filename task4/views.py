from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
def piatform (request):
    return render(request, 'platform.html')
def games (request):
    title = 'ИГРЫ'
    text = 'Вини Пух'
    text1 = 'Конёк горбунок'
    text2 = 'Дюймовочка'

    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077']

    }
    return render(request, 'games.html', context)

# def games (request):
#     return render(request, 'games.html')

def cart (request):
    return render(request, 'cart.html')




