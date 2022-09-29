from venv import create
from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name="index"),
    path('<int:id>', views.show, name="show"),
    path('create',views.create, name="create"),
    path('profile',views.profile, name="profile")
]
