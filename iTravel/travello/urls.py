
from django.urls import path
from . import views

app_name='Travello'

urlpatterns = [
    path('',views.homepage),
    path('dest/<int:dest_id>',views.dest_details,name='details')
]
