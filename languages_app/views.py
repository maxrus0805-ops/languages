from django.shortcuts import render, get_object_or_404
from .models import ProgrammingLanguage

def home(request):
    """Главная страница со всеми языками"""
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'index.html', {'languages': languages})

def language_detail(request, language_id):
    """Страница конкретного языка"""
    language = get_object_or_404(ProgrammingLanguage, id=language_id)
    return render(request, 'language.html', {'language': language})

def popular_languages(request):
    """Страница с популярными языками"""
    popular = ProgrammingLanguage.objects.filter(is_popular=True)[:5]
    return render(request, 'popular.html', {'popular_languages': popular})