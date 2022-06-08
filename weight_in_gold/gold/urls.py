from django.urls import path
from . import views

app_name = 'gold'
urlpatterns = [
	path('display.html', views.display, name='display')
]