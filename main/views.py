from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h4> ПРИВЕТ ЭТО ПЕРВЫЕ СЛОВА!!!</h4>")
