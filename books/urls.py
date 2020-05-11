from django.urls import path
from . views import scrape, books_list
from . import views


urlpatterns = [
    path('scrape/',views.scrape, name='scrape'),
    path('', views.books_list, name='home'),
]
