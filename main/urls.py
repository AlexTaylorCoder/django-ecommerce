from venv import create
from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name="index"),
<<<<<<< HEAD
=======
    path('<int:id>', views.show, name="show"),
    path('create',views.create, name="create")
>>>>>>> 1eeed5938902ccad1a83c8c5bffce95f6c440e45
]
