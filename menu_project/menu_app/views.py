from django.shortcuts import render


def menu_view(request):
    return render(request, 'menu_app/menu.html')
