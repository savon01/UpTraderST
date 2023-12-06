from django.urls import path
from menu_app.views import menu_view

app_name = 'menu_app'

urlpatterns = [
    path('menu/', menu_view, name='menu'),
]