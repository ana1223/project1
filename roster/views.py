from django.shortcuts import render
from roster.models import Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


def home(request):
    context = {
        'player_count': Player.objects.count(),
    }
    return render(request, "roster/home.html", context)

def player(request, pk):
    #player = Player.objects.order_by('?')[0]
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player':player})

def playerList(request):
    #player=Player.obects.orderby('?')
    player_list = Player.objects.all()
    
    return render(request, 'roster/player_list.html', {"players": player_list})

# Create your views here.
