from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def hello(request):
    return render(request,"index.html")
       
class formCreateView(CreateView):
    model = Dudas
    template_name = "index.html"
    fields = ["nombre", "apellido", "email", "dudas"]
    success_url = reverse_lazy("home")
    
class formCreateView2(CreateView):
    model = Suscripcion
    template_name = "index.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("home")