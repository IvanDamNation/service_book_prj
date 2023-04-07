from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, 'frontend_app/src/index.html')
