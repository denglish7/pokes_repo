from django.shortcuts import render, redirect
from .models import Poke
from ..login_reg_app.models import User
from django.contrib import messages
from django.db.models import Count

def index(request):
    if 'user_id' not in request.session:
        return redirect("login_reg:index")

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'pokes': User.objects.all(),
        'all_users': User.objects.all().exclude(id=request.session['user_id']),
        'user_pokes': Poke.objects.all().filter(pokee__id=request.session['user_id']),
        'pokers_of_user': User.objects.all().exclude(id=request.session['user_id']),
        'poke_history': Poke.objects.all(),
    }
    return render(request, "bb_app/index.html", context)

def poke(request, id):
    poker = User.objects.get(id=request.session['user_id'])
    pokee = User.objects.get(id=id)
    poke = Poke()
    poke.poker = poker
    poke.pokee = pokee
    poke.counter+=1
    poke.save()
    return redirect("bb_app:index")

def logoff(request):
    request.session.clear()
    return redirect("login_reg:index")
