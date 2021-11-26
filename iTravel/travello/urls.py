from django.contrib import admin
from django.urls import path,include
from . import views
app_name="Travello"
urlpatterns = [
    path('',views.homepage),
    path('dest/<int:id>',views.dest_details,name='details'),
    path('add',views.dest_add,name='add_destination'),
    path('api/dests',views.get_all_destinations)
]
