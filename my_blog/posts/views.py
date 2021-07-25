from django.shortcuts import render
from django.views.generic.base import View


class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'ricardo',
            'years': 28,
            'language': 'python'
        }
        return render(request, 'hello_word.html', context=data)