from django.shortcuts import render

def error_404_view(request):
    return render(request, 'medicos/404.html'
