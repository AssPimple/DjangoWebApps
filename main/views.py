from django.http import HttpResponse
from django.shortcuts import render
from typing import Dict, Any


def index(request) -> HttpResponse:
    context: Dict[str, Any] = {
        'title': 'Home',
        'content': 'Главная страница - Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')
