from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница !!!',
        'values': ['Ssomej', 'hello', '1234'],
        'obj': {
            'car': 'BMN',
            'age': 12,
            'hobby': 'football'

        }
    }
    return render(request, 'main/index.html',data)


def about(request):
    return render(request, 'main/about.html')
