from django.urls import path
from . import views
from CRUD_APP.views import *

urlpatterns = [
    path('', views.index, name='home'),

    ]