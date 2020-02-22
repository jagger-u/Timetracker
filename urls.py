from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='time-home'),
  path('insert', views.insert, name='time-insert'),
  path('insert/add', views.add, name='time-insert-add'),
  path('stats/', views.stats, name='time-stats'), 
  path('calendar/', views.calendar, name='time-calendar'), 
  path('stats/resultsdata/', views.resultsData, name='resultsdata'),
  path('particles/', views.particles, name='particles'),
]