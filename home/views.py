from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Home



# Create your views here.
def index(request, user_id):
    user_home = get_object_or_404(Home, pk = user_id)
    context = {
        'user' : user_home
    }
    return render(request, 'home/index.html', context)