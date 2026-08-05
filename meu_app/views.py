from django.shortcuts import render

# Esta é a nova view para a página inicial que usa os templates do exercício
def index(request):
    return render(request, 'meu_app/index.html')

# Sua view antiga (pode mantê-la ou removê-la)
def post_view(request):
    from django.http import HttpResponse
    return HttpResponse("Hello World")
    