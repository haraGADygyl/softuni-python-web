from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from softuni_python_web_basics.tasks.models import Task


# def home(request):
#     items = Task.objects.all()
#     item_string = [f'<li>{t.title}</li>' for t in items]
#     items_string = ''.join(item_string)
#     html = f'''
#     <h1>It really works!</h1>
#     <ul>
#         { items_string }
#     </ul>
#     '''
#
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'Works from views',
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)
