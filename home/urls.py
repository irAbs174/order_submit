from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (count_day_sall_dartil)

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
]
