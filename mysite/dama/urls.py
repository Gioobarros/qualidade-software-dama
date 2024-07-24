from . import views
from django.urls import path

app_name = 'dama'
urlpatterns = [
    path('dama/', views.IndexView.as_view(), name='index')
]