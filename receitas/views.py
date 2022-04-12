from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'receitas/home.html')

def sobre(request):
    return render(request, 'receitas/home.html')

def contato(request):
    return HttpResponse('Contato')
