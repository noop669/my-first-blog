from http.client import HTTPResponse
from django.shortcuts import render

from .models import translate
from .forms import TranslateForm

def translator(request):
    translater = translate
    if request.method == 'get':
        form = TranslateForm(request.get, instance = translater)
        return render(request, 'translate_django/django_translate.html', translater.translats())
    else:
        form = TranslateForm(instance = translater)
    return render(request, 'translate_django/django_translate.html', {'form': form})
