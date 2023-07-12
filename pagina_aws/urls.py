
from django.urls import path
from .views import formCreateView,formCreateView2
from . import views

urlpatterns = [
    path('home/', views.hello,name="home"),
    path("",formCreateView.as_view(), name="cuestionario" ) ,
    path("cuestionario2/",formCreateView2.as_view(), name="cuestionario2" ) ,
]
