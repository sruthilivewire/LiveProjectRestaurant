from django.urls import path
from . import views
from ACCOUNT.views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.Menu, name='menu'),
    path('AddItems/', views.Add_Food_Items_Form, name='add_food'),

    # Main-Course
    path('add-main-course/', views.Add_Main_Course, name='add-main-course'),
    path('delete_main_course/<int:id>', views.delete_main_course, name="delete_main_course"),
    path('update_main_course/<int:id>', views.update_main_course, name="update_main_course"),

    path('update_new_main_course/<int:id>', views.update_new_main_course, name="update_new_main_course"),

]

