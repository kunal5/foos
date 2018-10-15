from django.template import *
from django.http import *
from django.shortcuts import *
from .models import *
from operator import itemgetter
from .forms import *

def index(request):
	return render(request,'index.html')

def leaderboard(request):
	result = RegisterGame.objects.all()
	winner=dict()
	for res in result:
		if(res.team1_score > res.team2_score):
			if(res.team1.Team_Name in winner):
				winner[res.team1.Team_Name]+=1
			else:
				winner[res.team1.Team_Name]=1

		if(res.team2_score > res.team1_score):
			if(res.team2.Team_Name in winner):
				winner[res.team2.Team_Name]+=1
			else:
				winner[res.team2.Team_Name]=1

	sorted_teams = list(reversed(sorted(winner.items(), key=itemgetter(1))))
	return render(request,'leaderboard.html', {'teams': sorted_teams})

def team_list(request):
	teams = RegisterTeam.objects.all()
	return render(request,'team_list.html', {'team_list': teams})

def team_details(request, team_id):
	team = RegisterTeam.objects.get(pk=team_id)
	game = RegisterGame.objects.filter(team1=team).team1_score
	#game = RegisterGame.objects.all()
	return render(request, 'team_details.html', {'team': team, 'game':game})

def games(request):
	games = RegisterGame.objects.order_by('pk').reverse()
	return render(request, 'games.html', {'games': games})

def instructions(request):
	return render(request,'instructions.html')

def registerTeam(request):
	if request.method == "POST":
		form = RegisterTeamForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request,'index.html')

	else:
		form = RegisterTeamForm()
		return render(request, 'registerTeam.html', {'form': form})

def registerGame(request):
	if request.method == "POST":
		form = RegisterGameForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = RegisterGameForm()
		return render(request, 'registerGame.html', {'form': form})
