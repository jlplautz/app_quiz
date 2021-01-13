# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def indice(request):
    # return HttpResponse("Ola Plautz")
    return render(request, 'quizz/indice.html')


def perguntas(request):
    return render(request, 'quizz/pergunta.html')


def score(request):
    return render(request, 'quizz/score.html')
