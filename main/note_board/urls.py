from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('/notes', views.notes_page, name='notes')

]