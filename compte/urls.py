from django.urls import path
from . import views
urlpatterns = [
    path('inscription/',views.inscriptionPage,name="inscriptionPage"),
    path('acces/',views.accesPage,name="acces"),
    path('',views.home,name="home"),
    path('quitter/',views.logoutUser,name="quitter"),
]