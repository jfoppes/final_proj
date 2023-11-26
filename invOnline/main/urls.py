from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), # if there is no path defiend, show the default view/page
    path("login/",views.login, name="login"),
]