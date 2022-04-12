from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'receitas/pages/home.html')

def sobre(request):
    return render(request, 'receitas/pages/sobre.html')

def contato(request):
    return HttpResponse('Contato')
